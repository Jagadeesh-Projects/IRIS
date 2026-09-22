import json

from ollama import chat

from utils.logger import logger


class FileCommandParser:

    def __init__(self, model_name="qwen3:4b-instruct"):

        self.model_name = model_name

        logger.info(
            "File Command Parser initialized"
        )

    def parse(self, user_input):

        prompt = f"""
You are the file-command parser for IRIS.

Convert the user's natural-language file request
into JSON.

Allowed actions:

SEARCH
LIST

Return ONLY valid JSON.

JSON format:

{{
    "action": "SEARCH",
    "directory": null,
    "keyword": null,
    "extension": null
}}

Rules:

1. Use SEARCH when the user wants to find files.
2. Use LIST when the user wants to list files/folders.
3. If the user mentions Python files, use ".py".
4. If the user mentions PDF files, use ".pdf".
5. If the user mentions Word documents, use ".docx".
6. If the user mentions text files, use ".txt".
7. Extract a filename keyword when appropriate.
8. Do not invent a keyword.
9. Do not invent a directory.
10. Use null when a value is unknown.
11. Never include explanations.

Examples:

User:
Find Python files.

JSON:
{{
    "action": "SEARCH",
    "directory": null,
    "keyword": null,
    "extension": ".py"
}}

User:
Find Python files containing agent.

JSON:
{{
    "action": "SEARCH",
    "directory": null,
    "keyword": "agent",
    "extension": ".py"
}}

User:
Find PDF files.

JSON:
{{
    "action": "SEARCH",
    "directory": null,
    "keyword": null,
    "extension": ".pdf"
}}

User:
Find the resume file.

JSON:
{{
    "action": "SEARCH",
    "directory": null,
    "keyword": "resume",
    "extension": null
}}

User:
List files in my project.

JSON:
{{
    "action": "LIST",
    "directory": null,
    "keyword": null,
    "extension": null
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

            raw_response = response.message.content.strip()

            command = json.loads(raw_response)

            logger.info(
                f"Parsed file command: {command}"
            )

            return command

        except Exception as e:

            logger.error(
                f"File command parsing error: {e}"
            )

            return {
                "action": "SEARCH",
                "directory": None,
                "keyword": None,
                "extension": None
            }