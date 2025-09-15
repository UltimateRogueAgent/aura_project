from typing import Any, Dict, List
from crewai import Crew, Process, Task
from langchain_community.llms import Ollama
from ..agents import ResearcherAgent, CoderAgent, DesignerAgent, OrchestratorAgent

class Orchestrator:
    """
    Manages the CrewAI crew and the overall workflow for AURA.
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initializes the Orchestrator, including the LLM and all agents.

        Args:
            config: A dictionary containing the configuration for the orchestrator
                    and its components.
        """
        self.config = config
        self.llm = Ollama(model=config.get("llm_model", "rogue-v1-agent"))
        self.manager_llm = Ollama(model=config.get("manager_llm_model", "rogue-v1-brain"))

        # Initialize agents with their respective LLMs
        agent_config = self.config.get("agents", {})
        self.researcher = ResearcherAgent(agent_config.get("researcher", {}))
        self.coder = CoderAgent(agent_config.get("coder", {}))
        self.designer = DesignerAgent(agent_config.get("designer", {}))
        self.orchestrator_agent = OrchestratorAgent(agent_config.get("orchestrator", {}))

        # Assign LLMs to the crew_agent property of each agent instance
        self.researcher.crew_agent.llm = self.llm
        self.coder.crew_agent.llm = self.llm
        self.designer.crew_agent.llm = self.llm
        self.orchestrator_agent.crew_agent.llm = self.manager_llm


    def run_crew(self, user_request: str) -> str:
        """
        Runs the crew to process a user request. This involves creating tasks,
        assembling the crew, and kicking off the hierarchical process.

        Args:
            user_request: The user's request to be processed by the crew.

        Returns:
            The final result from the crew's execution.
        """
        # 1. Define tasks
        design_task = Task(
            description=f"Based on the user request: '{user_request}', create a detailed, step-by-step execution plan. The plan should be broken down into tasks that can be executed by a Coder Agent and a Researcher Agent.",
            agent=self.designer.crew_agent,
            expected_output="A list of tasks, with for each task a description, the assigned agent (Coder Agent or Researcher Agent) and the expected output."
        )

        # The hierarchical process will use the output of the design_task
        # to create and assign tasks to the other agents.

        # 2. Assemble the crew
        crew = Crew(
            agents=[self.designer.crew_agent, self.researcher.crew_agent, self.coder.crew_agent],
            tasks=[design_task],
            process=Process.hierarchical,
            manager_llm=self.manager_llm,
            manager_agent=self.orchestrator_agent.crew_agent
        )

        # 3. Kick off the crew's work
        result = crew.kickoff()
        return result
