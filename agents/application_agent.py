import re

from tools.tool_registry import get_tool

from utils.logger import logger


class ApplicationAgent:

    def __init__(self):

        logger.info(
            "Application Agent initialized"
        )

    def execute(self, user_input):

        application = self.extract_application(
            user_input
        )

        if application is None:

            return {
                "success": False,
                "error": (
                    "I couldn't determine which "
                    "application you want to open."
                )
            }

        tool = get_tool(
            "open_application"
        )

        if tool is None:

            return {
                "success": False,
                "error": "Application tool not found."
            }

        result = tool(
            application
        )

        return result

    def extract_application(self, user_input):

        text = user_input.lower()

        application_patterns = {

            "chrome": [
                r"\bchrome\b",
                r"\bgoogle chrome\b"
            ],

            "edge": [
                r"\bedge\b",
                r"\bmicrosoft edge\b"
            ],

            "notepad": [
                r"\bnotepad\b"
            ],

            "calculator": [
                r"\bcalculator\b",
                r"\bcalc\b"
            ],

            "paint": [
                r"\bpaint\b",
                r"\bmspaint\b"
            ],

            "vscode": [
                r"\bvs code\b",
                r"\bvisual studio code\b",
                r"\bvscode\b"
            ]
        }

        for application, patterns in (
            application_patterns.items()
        ):

            for pattern in patterns:

                if re.search(pattern, text):

                    return application

        return None