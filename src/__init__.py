"""Task Queue Manager - Advanced task queue management system."""

from typing import Dict, List, Any
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import uuid
import heapq
from collections import defaultdict


class AgentType(Enum):
    NVIDIA_GPU = "nvidia"
    AWS_TRAINIUM = "trainium"
    GOOGLE_TPU = "tpu"
    CPU = "cpu"


class Protocol(Enum):
    MCP = "mcp"
    A2A = "a2a"
    CUSTOM = "custom"
    HTTP = "http"


@dataclass
class Task:
    task_id: str
    data: Any
    priority: int = 0
    created_at: datetime = field(default_factory=datetime.now)
    
    def __lt__(self, other):
        return self.priority > other.priority


class TaskQueueManager:
    def __init__(self):
        self.queues: Dict[str, List[Task]] = defaultdict(list)
    
    def enqueue(self, queue_name: str, task_data: Any, priority: int = 0) -> str:
        task_id = str(uuid.uuid4())
        task = Task(task_id=task_id, data=task_data, priority=priority)
        heapq.heappush(self.queues[queue_name], task)
        return task_id
    
    def dequeue(self, queue_name: str) -> Task:
        if self.queues[queue_name]:
            return heapq.heappop(self.queues[queue_name])
        return None
    
    def peek(self, queue_name: str) -> Task:
        if self.queues[queue_name]:
            return self.queues[queue_name][0]
        return None
    
    def size(self, queue_name: str) -> int:
        return len(self.queues.get(queue_name, []))
    
    def get_stats(self) -> Dict[str, Any]:
        return {"queues": len(self.queues), "total_tasks": sum(len(q) for q in self.queues.values())}

__all__ = ["TaskQueueManager", "Task", "AgentType", "Protocol"]
