from ollama import chat

from utils.logger import logger


class IntentEngine:

    def __init__(self, model_name="qwen3:4b-instruct"):

        self.model_name = model_name

        logger.info(
            "Intent Engine initialized"
        )

    def detect(self, user_input):

        prompt = f"""
You are the intent detection module of IRIS,
a personal desktop AI assistant.

Classify the user's request into exactly ONE
of these intents:

GENERAL_QUERY
APPLICATION_CONTROL
FILE_OPERATION
SYSTEM_MONITORING
TASK_MANAGEMENT
REMINDER
MEMORY

Rules:

GENERAL_QUERY:
Questions, explanations, conversation,
or anything that does not require a computer action.

APPLICATION_CONTROL:
Opening, closing, launching, or controlling
desktop applications.

FILE_OPERATION:
Searching, creating, moving, deleting,
renaming, or reading files/folders.

SYSTEM_MONITORING:
CPU, RAM, disk, battery, system information,
or computer status.

TASK_MANAGEMENT:
Creating, modifying, completing, or organizing tasks.

REMINDER:
Setting a future reminder or notification.

MEMORY:
Saving, retrieving, updating, or forgetting
personal information or preferences.

Return ONLY the intent name.
Do not explain your answer.

User request:
{user_input}
"""

        try:

            response = chat(
                model=self.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            intent = response.message.content.strip()

            logger.info(
                f"Detected intent: {intent}"
            )

            return intent

        except Exception as e:

            logger.error(
                f"Intent detection error: {str(e)}"
            )

            return "GENERAL_QUERY"