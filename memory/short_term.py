from collections import deque

from utils.logger import logger


class ShortTermMemory:

    def __init__(self, max_messages=10):

        self.max_messages = max_messages

        self.messages = deque(
            maxlen=max_messages
        )

        logger.info(
            f"Short-term memory initialized with "
            f"maximum {max_messages} messages"
        )

    def add_message(
        self,
        role,
        content
    ):
        """
        Add a message to short-term memory.

        role:
            user
            assistant
            system
        """

        message = {
            "role": role,
            "content": content
        }

        self.messages.append(
            message
        )

        logger.info(
            f"Short-term memory added: {role}"
        )

    def get_messages(self):

        return list(
            self.messages
        )

    def get_recent_messages(
        self,
        count=5
    ):

        messages = list(
            self.messages
        )

        return messages[-count:]

    def clear(self):

        self.messages.clear()

        logger.info(
            "Short-term memory cleared"
        )

    def size(self):

        return len(
            self.messages
        )