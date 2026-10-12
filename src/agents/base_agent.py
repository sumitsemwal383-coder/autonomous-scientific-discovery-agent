"""
Base Agent Interface
Defines common execution lifecycle, messaging protocol, and state management
for all autonomous scientific discovery agents.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

class BaseAgent(ABC):
    def __init__(self, name: str, role: str, description: str):
        self.name = name
        self.role = role
        self.description = description
        self.state: Dict[str, Any] = {}
        self.execution_count = 0

    @abstractmethod
    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Core execution logic for the agent."""
        pass

    def log_action(self, action: str, details: Any) -> None:
        logger.info(f"[{self.role}] {action}: {details}")

    def get_status(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "role": self.role,
            "description": self.description,
            "execution_count": self.execution_count
        }
