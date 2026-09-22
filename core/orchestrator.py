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
        Context Engine for IRIS.

        Responsibilities:
        - Maintain recent conversation
        - Retrieve long-term memories
        - Detect simple memories from user messages
        - Limit context size
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
        Store user message in short-term memory.
        """

        self.short_term_memory.add_message(
            "user",
            message
        )

        # Try to extract useful persistent information
        self.extract_and_store_memory(message)

    def add_assistant_message(self, message):
        """
        Store assistant response in short-term memory.
        """

        self.short_term_memory.add_message(
            "assistant",
            message
        )

    def get_recent_conversation(self):
        """
        Return limited recent conversation.
        """

        messages = (
            self.short_term_memory
            .get_recent_messages()
        )

        if not messages:
            return []

        return messages[
            -self.max_recent_messages:
        ]

    # =========================================================
    # AUTOMATIC MEMORY EXTRACTION
    # =========================================================

    def extract_and_store_memory(self, message):
        """
        Detect simple facts from the user's message.

        This is intentionally rule-based for now.

        Supported examples:

        My name is Jagadeesh.
        I am working on IRIS.
        My project is IRIS.
        I like Python.
        """

        if not message:
            return

        text = str(message).strip()

        lower_text = text.lower()

        # -----------------------------------------------------
        # NAME
        # -----------------------------------------------------

        if lower_text.startswith("my name is "):

            value = text[
                len("my name is "):
            ].strip()

            if value:

                self.long_term_memory.remember(
                    "user",
                    "name",
                    value
                )

                return

        # -----------------------------------------------------
        # NAME - alternative format
        # -----------------------------------------------------

        if lower_text.startswith("i am "):

            value = text[
                len("i am "):
            ].strip()

            if value and len(value.split()) <= 5:

                # Avoid storing common conversational phrases
                ignored_values = [
                    "fine",
                    "good",
                    "okay",
                    "ok",
                    "tired",
                    "busy",
                    "happy",
                    "sad"
                ]

                if value.lower() not in ignored_values:

                    self.long_term_memory.remember(
                        "user",
                        "name",
                        value
                    )

                    return

        # -----------------------------------------------------
        # PROJECT
        # -----------------------------------------------------

        if lower_text.startswith(
            "my project is "
        ):

            value = text[
                len("my project is "):
            ].strip()

            if value:

                self.long_term_memory.remember(
                    "user",
                    "project",
                    value
                )

                return

        # -----------------------------------------------------
        # WORKING ON
        # -----------------------------------------------------

        if lower_text.startswith(
            "i am working on "
        ):

            value = text[
                len("i am working on "):
            ].strip()

            if value:

                self.long_term_memory.remember(
                    "user",
                    "project",
                    value
                )

                return

        # -----------------------------------------------------
        # LIKES
        # -----------------------------------------------------

        if lower_text.startswith(
            "i like "
        ):

            value = text[
                len("i like "):
            ].strip()

            if value:

                self.long_term_memory.remember(
                    "user",
                    "preference",
                    value
                )

                return

    # =========================================================
    # LONG-TERM MEMORY RETRIEVAL
    # =========================================================

    def get_relevant_memories(self, memories):
        """
        Retrieve selected long-term memories.

        Expected format:

        [
            ("user", "name"),
            ("user", "project")
        ]
        """

        relevant_memories = []

        for memory_type, key in memories:

            if (
                len(relevant_memories)
                >= self.max_memories
            ):
                break

            try:

                value = (
                    self.long_term_memory.recall(
                        memory_type,
                        key
                    )
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
    # AUTOMATIC MEMORY KEY SELECTION
    # =========================================================

    def find_memory_keys(self, user_input):
        """
        Find possible relevant memories.

        Uses simple keyword matching for now.
        """

        try:

            memories = (
                self.long_term_memory
                .all_memories()
            )

        except Exception:

            return []

        if not memories:

            return []

        user_input = str(
            user_input
        ).lower()

        relevant_keys = []

        # Common semantic keywords
        keyword_mapping = {

            "name": [
                "name",
                "who am i"
            ],

            "project": [
                "project",
                "building",
                "working on"
            ],

            "preference": [
                "like",
                "prefer",
                "favorite"
            ]
        }

        for memory_type, key, value in memories:

            if (
                len(relevant_keys)
                >= self.max_memories
            ):
                break

            key_text = str(
                key
            ).lower()

            value_text = str(
                value
            ).lower()

            # Direct key match
            if key_text in user_input:

                relevant_keys.append(
                    (memory_type, key)
                )

                continue

            # Stored value match
            if (
                value_text
                and value_text in user_input
            ):

                relevant_keys.append(
                    (memory_type, key)
                )

                continue

            # Keyword mapping
            if key_text in keyword_mapping:

                for keyword in keyword_mapping[
                    key_text
                ]:

                    if keyword in user_input:

                        relevant_keys.append(
                            (memory_type, key)
                        )

                        break

        return relevant_keys

    # =========================================================
    # TEXT LIMITER
    # =========================================================

    def limit_text(self, text):
        """
        Limit individual text size.
        """

        if text is None:

            return ""

        text = str(text)

        if (
            len(text)
            <= self.max_text_length
        ):

            return text

        return (
            text[
                :self.max_text_length
            ]
            + "\n...[content truncated]"
        )

    # =========================================================
    # CONTEXT SIZE CONTROL
    # =========================================================

    def limit_context(self, context):
        """
        Limit conversation and memory context.
        """

        # -----------------------------------------------------
        # Current input
        # -----------------------------------------------------

        context["current_input"] = (
            self.limit_text(
                context.get(
                    "current_input",
                    ""
                )
            )
        )

        # -----------------------------------------------------
        # Recent conversation
        # -----------------------------------------------------

        recent_conversation = (
            context.get(
                "recent_conversation",
                []
            )
        )

        limited_conversation = []

        for message in recent_conversation:

            if isinstance(
                message,
                dict
            ):

                item = dict(message)

                if "content" in item:

                    item["content"] = (
                        self.limit_text(
                            item["content"]
                        )
                    )

                limited_conversation.append(
                    item
                )

            else:

                limited_conversation.append(
                    self.limit_text(
                        message
                    )
                )

        context[
            "recent_conversation"
        ] = limited_conversation[
            -self.max_recent_messages:
        ]

        # -----------------------------------------------------
        # Long-term memories
        # -----------------------------------------------------

        memories = (
            context.get(
                "relevant_memories",
                []
            )
        )

        limited_memories = []

        for memory in memories[
            :self.max_memories
        ]:

            if isinstance(
                memory,
                dict
            ):

                item = dict(memory)

                if "value" in item:

                    item["value"] = (
                        self.limit_text(
                            item["value"]
                        )
                    )

                limited_memories.append(
                    item
                )

            else:

                limited_memories.append(
                    self.limit_text(
                        memory
                    )
                )

        context[
            "relevant_memories"
        ] = limited_memories

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
        Build the complete context.

        1. Current request
        2. Recent conversation
        3. Relevant long-term memories
        4. Context size control
        """

        if memory_keys is None:

            memory_keys = (
                self.find_memory_keys(
                    user_input
                )
            )

        recent_conversation = (
            self.get_recent_conversation()
        )

        relevant_memories = (
            self.get_relevant_memories(
                memory_keys
            )
        )

        context = {

            "current_input":
                user_input,

            "recent_conversation":
                recent_conversation,

            "relevant_memories":
                relevant_memories
        }

        return self.limit_context(
            context
        )