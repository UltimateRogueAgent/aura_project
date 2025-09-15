from typing import Any, Dict, List
from crewai import Agent
from .base_agent import BaseAgent
from ..tools import web_scraper_tool, search_tool

class ResearcherAgent(BaseAgent):
    """
    A specialized agent responsible for finding and analyzing information
    on the web. It uses web scraping and search tools to gather data.
    """

    def _create_crew_agent(self) -> Agent:
        """
        Creates and configures the CrewAI Agent for the Researcher.
        """
        return Agent(
            role=self.config.get("role", "Web Researcher"),
            goal=self.config.get("goal", "Find and analyze information on the web based on a given topic."),
            backstory=self.config.get(
                "backstory",
                "You are an expert web researcher, skilled in using search engines and scraping tools to find the most relevant and accurate information."
            ),
            tools=self.tools,
            allow_delegation=False,
            verbose=True,
        )

    def setup_tools(self) -> List[Any]:
        """
        Sets up the tools for the ResearcherAgent.
        """
        # These tools are imported from aura_project.tools
        return [web_scraper_tool, search_tool]

    def get_capabilities(self) -> List[str]:
        """
        Returns the capabilities of the ResearcherAgent.
        """
        return ["web_search", "web_scraping"]
