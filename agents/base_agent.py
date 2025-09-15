from abc import ABC, abstractmethod
from typing import Any, Dict, List
from crewai import Agent, Task
from ..core.models import TaskResult

class BaseAgent(ABC):
    """
    Abstract base class for all specialized agents in the AURA system.
    This class provides a common structure and interface for agent creation,
    tool setup, and task execution within the CrewAI framework.
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initializes the base agent.

        Args:
            config: A dictionary containing configuration for the agent,
                    such as model, role, goal, and backstory.
        """
        self.config = config
        self.tools = self.setup_tools()
        self.crew_agent = self._create_crew_agent()

    @abstractmethod
    def _create_crew_agent(self) -> Agent:
        """
        Creates and configures the underlying crewai.Agent.
        This method should be implemented by each specialized agent class.
        """
        pass

    @abstractmethod
    def setup_tools(self) -> List[Any]:
        """
        Sets up and returns the list of tools available to the agent.
        This method should be implemented by each specialized agent class.
        """
        pass

    def execute_task(self, task: Task) -> TaskResult:
        """
        Executes a given task using the crewAI agent.
        Note: In CrewAI, task execution is typically managed by the Crew,
        which orchestrates the flow of tasks between agents. This method
        serves as a conceptual placeholder for task execution logic
        that might be needed for monitoring or logging at the agent level.
        """
        print(f"Agent '{self.crew_agent.role}' is conceptually executing task: {task.description}")

        # The actual result of the task execution is handled by the Crew's kickoff process.
        # This method returns a placeholder TaskResult.
        return TaskResult(
            task_id=str(task.id),  # Assuming task has an id attribute
            success=True, # Placeholder status
            result="Task execution is managed by the Crew. This is a conceptual placeholder.",
            execution_time=0.0,
            agent_logs=[f"Task '{task.description}' assigned to agent '{self.crew_agent.role}'."]
        )

    @abstractmethod
    def get_capabilities(self) -> List[str]:
        """
        Returns a list of capabilities or specializations of the agent.
        """
        pass
