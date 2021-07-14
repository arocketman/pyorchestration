from app.core.orchestrate import OrchestrationState, Orchestration
from app.state import factory
import sample_steps


class MyState(OrchestrationState):

    def __init__(self, name):
        self.name = name
        self.age = 0

    @classmethod
    def from_dict(cls, payload):
        return cls(name=payload.get('name', 'noname'))

def trigger_orchestration(name, payload):
    factory.get(name).orchestrate(payload)

if __name__ == '__main__':
    payload = {
        'name': 'Andrea'
    }
    trigger_orchestration('default_orchestration', payload)