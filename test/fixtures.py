from app.core.orchestrate import OrchestrationState


class TestState(OrchestrationState):

    def __init__(self, name):
        self.name = name
        self.age = 0

    @classmethod
    def from_dict(cls, payload):
        return cls(name=payload.get('name', 'noname'))
