from pyorchestration.core.commons import OrchestrationState
from pyorchestration.core.engine import Orchestration


class OrchestratorFactory:

    def __init__(self):
        self.orchestrations = {}

    def get(self, name: str) -> Orchestration:
        return self.orchestrations.get(name, None)

    def register(self, name: str, state_class: OrchestrationState, config_file=''):
        print(f'Registering new orchestration {name}')
        self.orchestrations[name] = Orchestration(name, state_class, config_file)
        return self.get(name)


factory = OrchestratorFactory()
