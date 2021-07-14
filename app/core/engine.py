import json
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

    def execute_step(self, step: Step, state: OrchestrationState):
        step.func(state)