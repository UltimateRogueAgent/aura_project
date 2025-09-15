from typing import Any, Dict, List
from crewai import Agent
from .base_agent import BaseAgent
from ..tools import MCPTools
from ..integrations import MCPClient

# Note: Memory tools will be implemented in a later task as per tasks.md (12.2)
# from ..tools import memory_search_tool, memory_save_tool

class DesignerAgent(BaseAgent):
    """
    A specialized agent responsible for designing and planning solutions.
    It breaks down complex problems into smaller, manageable tasks.
    """

    def _create_crew_agent(self) -> Agent:
        """
        Creates and configures the CrewAI Agent for the Designer.
        """
        return Agent(
            role=self.config.get("role", "Solution Architect"),
            goal=self.config.get("goal", "Design and plan solutions to complex problems by breaking them down into smaller tasks."),
            backstory=self.config.get(
                "backstory",
                "You are an expert solution architect, skilled in system design and task planning. You create clear and concise plans for other agents to follow."
            ),
            tools=self.tools,
            allow_delegation=True,  # The designer can delegate tasks to other agents
            verbose=True,
        )

    def setup_tools(self) -> List[Any]:
        """
        Sets up the tools for the DesignerAgent.
        """
        tools = []

        # Setup for MCPTools if mcp_client is provided in config
        if "mcp_client" in self.config:
            mcp_client = self.config["mcp_client"]
            if isinstance(mcp_client, MCPClient):
                 mcp_tools_config = self.config.get("mcp_tools_config", {})
                 tools.append(MCPTools(config=mcp_tools_config, mcp_client=mcp_client))

        # Placeholder for memory tools to be added in task 12.2
        # For now, we can add a comment to remember this.
        # tools.extend([memory_search_tool, memory_save_tool])

        return tools

    def get_capabilities(self) -> List[str]:
        """
        Returns the capabilities of the DesignerAgent.
        """
        return ["solution_design", "task_planning", "system_architecture"]
