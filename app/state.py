from app.core.orchestrate import Orchestration

class OrchestratorFactory:

  def __init__(self):
    self.orchestrations = {}

  def register(self, orchestration):
    print(f'Registering new orchestration {orchestration.name}')
    self.orchestrations[orchestration.name] = orchestration
    
  def get(self, name: str, state_class = '') -> Orchestration:
    if name not in self.orchestrations:
      print(f'Registering new orchestration {name}')
      self.orchestrations[name] = Orchestration(name, state_class)
    
    return self.orchestrations[name]

factory = OrchestratorFactory()