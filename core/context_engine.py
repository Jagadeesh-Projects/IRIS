from memory.short_term import ShortTermMemory
from memory.long_term import LongTermMemory


class ContextEngine:

    def __init__(
        self,
        max_recent_messages=10,
        max_memories=10,
        max_text_length=4000
    ):
        """
        Initialize the Context Engine.

        Parameters:
            max_recent_messages:
                Maximum number of recent conversation messages.

            max_memories:
                Maximum number of long-term memories.

            max_text_length:
                Maximum length of a single text item.
        """

        self.short_term_memory = ShortTermMemory()
        self.long_term_memory = LongTermMemory()

        self.max_recent_messages = max_recent_messages
        self.max_memories = max_memories
        self.max_text_length = max_text_length

    # =========================================================
    # SHORT-TERM MEMORY
    # =========================================================

    def add_user_message(self, message):
        """
        Store a user message in short-term memory.
        """

        self.short_term_memory.add_message(
            "user",
            message
        )

    def add_assistant_message(self, message):
        """
        Store an assistant response in short-term memory.
        """

        self.short_term_memory.add_message(
            "assistant",
            message
        )

    def get_recent_conversation(self):
        """
        Get only a limited number of recent messages.
        """

        messages = self.short_term_memory.get_recent_messages()

        if not messages:
            return []

        return messages[-self.max_recent_messages:]

    # =========================================================
    # LONG-TERM MEMORY
    # =========================================================

    def get_relevant_memories(self, memories):
        """
        Retrieve selected long-term memories.
        """

        relevant_memories = []

        for memory_type, key in memories:

            if len(relevant_memories) >= self.max_memories:
                break

            try:

                value = self.long_term_memory.recall(
                    memory_type,
                    key
                )

                if value is not None:

                    relevant_memories.append(
                        {
                            "type": memory_type,
                            "key": key,
                            "value": value
                        }
                    )

            except Exception:
                continue

        return relevant_memories

    # =========================================================
    # AUTOMATIC MEMORY SELECTION
    # =========================================================

    def find_memory_keys(self, user_input):
        """
        Automatically find possible relevant memories.
        """

        try:

            memories = self.long_term_memory.all_memories()

        except Exception:

            return []

        if not memories:
            return []

        user_input = str(user_input).lower()

        relevant_keys = []

        for memory_type, key, value in memories:

            if len(relevant_keys) >= self.max_memories:
                break

            key_text = str(key).lower()
            value_text = str(value).lower()

            # Direct key match
            if key_text in user_input:

                relevant_keys.append(
                    (memory_type, key)
                )

                continue

            # Direct value match
            if value_text and value_text in user_input:

                relevant_keys.append(
                    (memory_type, key)
                )

        return relevant_keys

    # =========================================================
    # TEXT LIMITER
    # =========================================================

    def limit_text(self, text):
        """
        Prevent an individual text value from becoming
        excessively large.
        """

        if text is None:
            return ""

        text = str(text)

        if len(text) <= self.max_text_length:
            return text

        return (
            text[:self.max_text_length]
            + "\n...[content truncated]"
        )

    # =========================================================
    # CONTEXT SIZE CONTROL
    # =========================================================

    def limit_context(self, context):
        """
        Limit the size of the complete context.

        This prevents very large tool/file outputs from
        being sent directly to the LLM.
        """

        # -----------------------------------------------------
        # Limit current input
        # -----------------------------------------------------

        context["current_input"] = self.limit_text(
            context.get("current_input", "")
        )

        # -----------------------------------------------------
        # Limit recent conversation
        # -----------------------------------------------------

        recent_conversation = context.get(
            "recent_conversation",
            []
        )

        limited_conversation = []

        for message in recent_conversation:

            if isinstance(message, dict):

                limited_message = dict(message)

                if "content" in limited_message:

                    limited_message["content"] = (
                        self.limit_text(
                            limited_message["content"]
                        )
                    )

                limited_conversation.append(
                    limited_message
                )

            else:

                limited_conversation.append(
                    self.limit_text(message)
                )

        context["recent_conversation"] = (
            limited_conversation[
                -self.max_recent_messages:
            ]
        )

        # -----------------------------------------------------
        # Limit long-term memories
        # -----------------------------------------------------

        memories = context.get(
            "relevant_memories",
            []
        )

        limited_memories = []

        for memory in memories[:self.max_memories]:

            if isinstance(memory, dict):

                limited_memory = dict(memory)

                if "value" in limited_memory:

                    limited_memory["value"] = (
                        self.limit_text(
                            limited_memory["value"]
                        )
                    )

                limited_memories.append(
                    limited_memory
                )

            else:

                limited_memories.append(
                    self.limit_text(memory)
                )

        context["relevant_memories"] = (
            limited_memories
        )

        return context

    # =========================================================
    # BUILD CONTEXT
    # =========================================================

    def build_context(
        self,
        user_input,
        memory_keys=None
    ):
        """
        Build safe, bounded context.

        Steps:

        1. Receive user request
        2. Retrieve recent conversation
        3. Find relevant long-term memories
        4. Limit context
        5. Return final context
        """

        # -----------------------------------------------------
        # Find memories automatically
        # -----------------------------------------------------

        if memory_keys is None:

            memory_keys = self.find_memory_keys(
                user_input
            )

        # -----------------------------------------------------
        # Get recent conversation
        # -----------------------------------------------------

        recent_conversation = (
            self.get_recent_conversation()
        )

        # -----------------------------------------------------
        # Get long-term memories
        # -----------------------------------------------------

        relevant_memories = (
            self.get_relevant_memories(
                memory_keys
            )
        )

        # -----------------------------------------------------
        # Create context
        # -----------------------------------------------------

        context = {
            "current_input": user_input,
            "recent_conversation": recent_conversation,
            "relevant_memories": relevant_memories
        }

        # -----------------------------------------------------
        # Apply size limits
        # -----------------------------------------------------

        context = self.limit_context(
            context
        )

        return context