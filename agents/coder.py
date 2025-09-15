from typing import Any, Dict, List
from crewai import Agent
from .base_agent import BaseAgent
from ..tools import FileTools

class CoderAgent(BaseAgent):
    """
    A specialized agent responsible for writing, managing, and debugging code.
    It uses file system tools to interact with the workspace.
    """

    def _create_crew_agent(self) -> Agent:
        """
        Creates and configures the CrewAI Agent for the Coder.
        """
        return Agent(
            role=self.config.get("role", "Software Engineer"),
            goal=self.config.get("goal", "Write, debug, and manage code according to specifications."),
            backstory=self.config.get(
                "backstory",
                "You are a senior software engineer, specializing in writing clean, efficient, and well-documented code."
            ),
            tools=self.tools,
            allow_delegation=False,
            verbose=True,
        )

    def setup_tools(self) -> List[Any]:
        """
        Sets up the tools for the CoderAgent.
        """
        # The config for FileTools, such as sandbox_path, will be passed
        # during the agent's initialization.
        file_tools_config = self.config.get("file_tools_config", {})
        return [FileTools(config=file_tools_config)]

    def get_capabilities(self) -> List[str]:
        """
        Returns the capabilities of the CoderAgent.
        """
        return ["file_system_access", "code_writing", "code_debugging"]
