from tools.tool_registry import get_tool

from utils.logger import logger


class SystemAgent:

    def __init__(self):

        logger.info(
            "System Agent initialized"
        )

    def execute(self, user_input):

        tool = get_tool(
            "get_system_info"
        )

        if tool is None:

            return {
                "success": False,
                "error": "System information tool not found."
            }

        try:

            result = tool()

            return {
                "success": True,
                "data": result
            }

        except Exception as e:

            logger.error(
                f"System Agent error: {e}"
            )

            return {
                "success": False,
                "error": str(e)
            }