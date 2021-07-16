from abc import ABC, abstractmethod
from typing import Callable

from pyorchestration.core.exceptions import IllegalOrchestrationGraphException


class OrchestrationState(ABC):

    def __init__(self, cfg=None):
        """
        Abstract State, to be overridden for custom states usage
        """
        if cfg is None:
            cfg = {}

        self.cfg = cfg

    @classmethod
    @abstractmethod
    def from_dict(cls, payload):
        pass


class Step:

    def __init__(self, step_number: int, func: Callable, skippable=False):
        """
        Encapsulates a step
        """
        self.step_number = step_number
        self.func = func
        self.skippable = skippable

    def __str__(self) -> str:
        return f'({self.step_number} | {self.func.__name__})'

    def __repr__(self) -> str:
        return str(self)

    def __lt__(self, other):
        if self.step_number == other.step_number:
            raise IllegalOrchestrationGraphException('Step numbers cannot be the same for a given orchestration!')

        return self.step_number < other.step_number

