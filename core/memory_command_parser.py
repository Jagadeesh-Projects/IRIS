import json

from ollama import chat

from utils.logger import logger


class MemoryCommandParser:

    def __init__(
        self,
        model_name="qwen3:4b-instruct"
    ):

        self.model_name = model_name

        logger.info(
            "Memory Command Parser initialized"
        )

    def parse(self, user_input):

        prompt = f"""
You are the memory command parser for IRIS.

Convert the user's request into JSON.

Allowed actions:

SAVE
RECALL

Return ONLY valid JSON.

Format:

{{
    "action": "SAVE",
    "memory_type": null,
    "key": null,
    "value": null
}}

Rules:

1. Use SAVE when the user wants IRIS to remember something.
2. Use RECALL when the user asks IRIS to retrieve something.
3. Extract the important memory type.
4. Extract a concise key.
5. For SAVE, extract the value.
6. For RECALL, value should be null.
7. Never invent information.
8. Do not include explanations.

Examples:

User:
Remember that I prefer Python.

JSON:
{{
    "action": "SAVE",
    "memory_type": "preference",
    "key": "programming_language",
    "value": "Python"
}}

User:
My name is Jagadeesh.

JSON:
{{
    "action": "SAVE",
    "memory_type": "user",
    "key": "name",
    "value": "Jagadeesh"
}}

User:
What programming language do I prefer?

JSON:
{{
    "action": "RECALL",
    "memory_type": "preference",
    "key": "programming_language",
    "value": null
}}

User:
What is my name?

JSON:
{{
    "action": "RECALL",
    "memory_type": "user",
    "key": "name",
    "value": null
}}

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
                ],
                format="json"
            )

            command = json.loads(
                response.message.content
            )

            logger.info(
                f"Parsed memory command: {command}"
            )

            return command

        except Exception as e:

            logger.error(
                f"Memory parsing error: {e}"
            )

            return {
                "action": "RECALL",
                "memory_type": None,
                "key": None,
                "value": None
            }