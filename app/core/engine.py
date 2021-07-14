import json
import logging
from typing import List
from app.core.commons import OrchestrationState, Step


class Orchestration:

    def __init__(self, name, state_class):
        self.name = name
        self.state_class = state_class
        self.steps: List[Step] = []

    def orchestrate(self, payload):
        state: OrchestrationState = self.state_class.from_dict(json.loads(payload))
        for step in sorted(self.steps):
            self.execute_step(step, state)

        return state

    def execute_step(self, step: Step, state: OrchestrationState):
        try:
            step.func(state)
        except Exception as e:
            if step.skippable:
                logging.exception(f"Exception in step {step.func.__name__}, marked as skippable.. continuing..")
            else:
                raise
