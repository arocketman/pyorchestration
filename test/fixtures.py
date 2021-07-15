from pyorchestration.core.commons import OrchestrationState


class TestState(OrchestrationState):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.age = 0

    @classmethod
    def from_dict(cls, payload):
        return cls(name=payload.get('name', 'noname'))
