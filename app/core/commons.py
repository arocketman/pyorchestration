from abc import ABC, abstractmethod
from typing import Callable


class OrchestrationState(ABC):

    @classmethod
    @abstractmethod
    def from_dict(cls, payload):
        pass


class Step:

    def __init__(self, step_number: int, func: Callable, skippable=False):
        self.step_number = step_number
        self.func = func
        self.skippable = skippable

    def __str__(self) -> str:
        return f'({self.step_number} | {self.func.__name__})'

    def __repr__(self) -> str:
        return str(self)

    def __lt__(self, other):
        return self.step_number < other.step_number

