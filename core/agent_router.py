from agents.system_agent import SystemAgent
from agents.file_agent import FileAgent
from agents.application_agent import ApplicationAgent
from agents.memory_agent import MemoryAgent

from utils.logger import logger


class AgentRouter:

    def __init__(self):

        self.agents = {

            "SYSTEM_MONITORING":
                SystemAgent(),

            "FILE_OPERATION":
                FileAgent(),

            "APPLICATION_CONTROL":
                ApplicationAgent(),

            "MEMORY":
                MemoryAgent()

        }

        logger.info(
            "Agent Router initialized"
        )

    def get_agent(self, intent):

        agent = self.agents.get(intent)

        if agent is None:

            logger.warning(
                f"No agent found for intent: {intent}"
            )

        return agent