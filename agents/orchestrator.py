from typing import Any, Dict, List
from crewai import Agent
from .base_agent import BaseAgent

class OrchestratorAgent(BaseAgent):
    """
    The manager agent for the CrewAI crew. This agent oversees the work
    of the other specialized agents and ensures the project is completed.
    """

    def _create_crew_agent(self) -> Agent:
        """
        Creates and configures the CrewAI Agent for the Orchestrator.
        """
        return Agent(
            role=self.config.get("role", "Project Manager"),
            goal=self.config.get("goal", "Oversee the work of the other agents to ensure the successful completion of the project."),
            backstory=self.config.get(
                "backstory",
                "You are an expert project manager, skilled in coordinating teams of specialists to achieve a common goal."
            ),
            tools=self.tools,
            allow_delegation=True,
            verbose=True,
        )

    def setup_tools(self) -> List[Any]:
        """
        Sets up the tools for the OrchestratorAgent.
        The orchestrator itself might not need tools, as its primary role is to manage.
        """
        return []

    def get_capabilities(self) -> List[str]:
        """
        Returns the capabilities of the OrchestratorAgent.
        """
        return ["project_management", "coordination", "delegation"]
