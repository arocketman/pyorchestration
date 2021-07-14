from app.core.engine import Orchestration


class OrchestratorFactory:

    def __init__(self):
        self.orchestrations = {}

    def get(self, name: str, state_class='') -> Orchestration:
        if name not in self.orchestrations:
            print(f'Registering new orchestration {name}')
            self.orchestrations[name] = Orchestration(name, state_class)

        return self.orchestrations[name]


factory = OrchestratorFactory()
