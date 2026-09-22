import os

from core.file_command_parser import FileCommandParser

from tools.tool_registry import get_tool

from utils.logger import logger


class FileAgent:

    def __init__(self):

        logger.info(
            "File Agent initialized"
        )

        self.parser = FileCommandParser()

        self.base_directory = r"E:\IRIS"

    def execute(self, user_input):

        try:

            command = self.parser.parse(
                user_input
            )

            action = command.get(
                "action",
                "SEARCH"
            )

            directory = command.get(
                "directory"
            )

            keyword = command.get(
                "keyword"
            )

            extension = command.get(
                "extension"
            )

            # For now, all file operations are
            # restricted to the IRIS project.
            if not directory:

                directory = self.base_directory

            # Security boundary:
            # File Agent may only operate inside
            # the configured IRIS project directory.
            directory = os.path.abspath(
                directory
            )

            base_directory = os.path.abspath(
                self.base_directory
            )

            if not (
                directory == base_directory
                or directory.startswith(
                    base_directory + os.sep
                )
            ):

                return {
                    "success": False,
                    "error": "Directory is outside the allowed IRIS project."
                }

            # SEARCH
            if action == "SEARCH":

                tool = get_tool(
                    "search_files"
                )

                if tool is None:

                    return {
                        "success": False,
                        "error": "Search tool not found."
                    }

                result = tool(
                    directory=directory,
                    keyword=keyword or "",
                    extension=extension,
                    max_results=50
                )

                if not result.get("success"):

                    return {
                        "success": False,
                        "error": result.get(
                            "error",
                            "File search failed."
                        )
                    }

                return {
                    "success": True,
                    "data": {
                        "action": "SEARCH",
                        "count": result.get(
                            "count",
                            0
                        ),
                        "files": result.get(
                            "files",
                            []
                        )
                    }
                }

            # LIST
            if action == "LIST":

                tool = get_tool(
                    "list_directory"
                )

                if tool is None:

                    return {
                        "success": False,
                        "error": "Directory listing tool not found."
                    }

                result = tool(
                    directory=directory,
                    max_results=50
                )

                if not result.get("success"):

                    return {
                        "success": False,
                        "error": result.get(
                            "error",
                            "Directory listing failed."
                        )
                    }

                return {
                    "success": True,
                    "data": {
                        "action": "LIST",
                        "count": result.get(
                            "count",
                            0
                        ),
                        "items": result.get(
                            "items",
                            []
                        )
                    }
                }

            return {
                "success": False,
                "error": f"Unsupported file action: {action}"
            }

        except Exception as e:

            logger.error(
                f"File Agent error: {e}"
            )

            return {
                "success": False,
                "error": str(e)
            }