from memory.database import MemoryDatabase

from utils.logger import logger


class LongTermMemory:

    def __init__(self):

        self.database = MemoryDatabase()

        logger.info(
            "Long-term memory initialized"
        )

    def remember(
        self,
        memory_type,
        key,
        value
    ):

        return self.database.save_memory(
            memory_type,
            key,
            value
        )

    def recall(
        self,
        memory_type,
        key
    ):

        return self.database.get_memory(
            memory_type,
            key
        )

    def all_memories(
        self,
        memory_type=None
    ):

        return self.database.get_all_memories(
            memory_type
        )