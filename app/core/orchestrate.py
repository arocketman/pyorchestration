from abc import ABC, abstractmethod
from typing import Callable, List

class OrchestrationState(ABC):

    @classmethod
    @abstractmethod
    def from_dict(cls, payload):
        pass

class Orchestration:

    def __init__(self, name, state_class):
        self.name = name
        self.state_class = state_class
        self.steps: List[Step] = []

    def orchestrate(self, payload):
        state: OrchestrationState = self.state_class.from_dict(payload)
        self.steps.sort()
        for step in self.steps:
            step.func(state)

class Step:
    
    def __init__(self, step_number: int, func: Callable):
      self.step_number = step_number
      self.func = func

    def __str__(self) -> str:
        return f'({self.step_number} | {self.func.__name__})'

    
    def __repr__(self) -> str:
        return str(self)

    def __lt__(self, other):
        return self.step_number < other.step_number