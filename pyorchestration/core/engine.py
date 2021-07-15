import json
import logging
from typing import List

import yaml

from pyorchestration.core.commons import OrchestrationState, Step


class Orchestration:

    def __init__(self, name, state_class, config_file=None):
        self.name = name
        self.state_class = state_class
        self.steps: List[Step] = []
        self.cfg = {}
        if config_file:
            with open(config_file) as fp:
                self.cfg = yaml.safe_load(fp)

    def orchestrate(self, payload):
        state: OrchestrationState = self.state_class.from_dict(json.loads(payload))
        state.cfg = self.cfg
        for step in sorted(self.steps):
            self.execute_step(step, state)

        return state

    def execute_step(self, step: Step, state: OrchestrationState):
        try:
            step.func(state)
        except Exception as e:
            if step.skippable:
                logging.exception(f"Exception in orchestration {self.name}, step {step.func.__name__}, marked as skippable.. continuing..")
            else:
                raise
