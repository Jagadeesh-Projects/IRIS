from ollama import chat

from memory.short_term import ShortTermMemory

from utils.logger import logger


class ModelManager:

    def __init__(
        self,
        model_name="qwen3:4b-instruct"
    ):

        self.model_name = model_name

        self.short_term_memory = (
            ShortTermMemory(
                max_messages=10
            )
        )

        self.system_prompt = """
You are IRIS, a personal desktop AI assistant.

Your job is to assist the user with:
- General questions
- Learning
- Productivity
- Computer tasks
- File management
- Application control
- Task planning
- Personal organization

Rules:
1. Be helpful and concise.
2. Understand the user's request before responding.
3. Never claim that you performed an action unless
   a real tool has actually executed that action.
4. When a request requires a computer action, clearly
   explain what needs to be done.
5. Do not invent information about the user's computer.
6. Treat the user as the owner of the computer and
   their data.
"""

        logger.info(
            f"Model Manager initialized: "
            f"{self.model_name}"
        )

    def generate_response(
        self,
        user_input
    ):

        try:

            messages = [
                {
                    "role": "system",
                    "content": self.system_prompt
                }
            ]

            # Add recent conversation
            messages.extend(
                self.short_term_memory
                .get_recent_messages(
                    count=10
                )
            )

            # Add current user message
            messages.append(
                {
                    "role": "user",
                    "content": user_input
                }
            )

            response = chat(
                model=self.model_name,
                messages=messages
            )

            answer = response.message.content

            # Store current conversation
            self.short_term_memory.add_message(
                "user",
                user_input
            )

            self.short_term_memory.add_message(
                "assistant",
                answer
            )

            logger.info(
                "AI response generated successfully"
            )

            return answer

        except Exception as e:

            logger.error(
                f"AI model error: {str(e)}"
            )

            return (
                "I'm having trouble connecting to "
                "my local AI model."
            )