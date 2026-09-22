from core.memory_command_parser import MemoryCommandParser
from memory.long_term import LongTermMemory

from utils.logger import logger


class MemoryAgent:

    def __init__(self):

        self.memory = LongTermMemory()
        self.parser = MemoryCommandParser()

        logger.info(
            "Memory Agent initialized"
        )

    def execute(self, user_input):

        try:

            command = self.parser.parse(
                user_input
            )

            action = command.get("action")
            memory_type = command.get("memory_type")
            key = command.get("key")
            value = command.get("value")

            if not memory_type or not key:

                return {
                    "success": False,
                    "error": "I couldn't determine what memory to use."
                }

            if action == "SAVE":

                if value is None:

                    return {
                        "success": False,
                        "error": "No memory value was provided."
                    }

                self.memory.remember(
                    memory_type,
                    key,
                    value
                )

                return {
                    "success": True,
                    "data": {
                        "action": "SAVE",
                        "memory_type": memory_type,
                        "key": key,
                        "value": value
                    }
                }

            if action == "RECALL":

                stored_value = self.memory.recall(
                    memory_type,
                    key
                )

                return {
                    "success": True,
                    "data": {
                        "action": "RECALL",
                        "memory_type": memory_type,
                        "key": key,
                        "value": stored_value
                    }
                }

            return {
                "success": False,
                "error": f"Unsupported memory action: {action}"
            }

        except Exception as e:

            logger.error(
                f"Memory Agent error: {e}"
            )

            return {
                "success": False,
                "error": str(e)
            }