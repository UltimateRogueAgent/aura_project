from dataclasses import dataclass
from typing import List, Optional, Any, Dict
from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    """
    Represents the status of a task.
    """
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class TaskRequest:
    """
    Represents a request to perform a task.
    """
    id: str
    user_input: str
    timestamp: datetime
    priority: int = 1

@dataclass
class TaskStep:
    """
    Represents a single step within a larger task.
    """
    id: str
    agent: str
    description: str
    dependencies: List[str]
    status: TaskStatus
    result: Optional[str] = None

@dataclass
class TaskResult:
    """
    Represents the result of a completed task.
    """
    task_id: str
    success: bool
    result: str
    execution_time: float
    agent_logs: List[str]
