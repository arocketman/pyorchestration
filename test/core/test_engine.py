from test.fixtures import TestState
from app.core.decorators  import step
from app.core.engine import Orchestration
from app.state import factory

@step(1, state_class=TestState)
def correct_step(state_object: TestState):
    state_object.name = 'hello_test'

def test_execute_correct_step():
    orchestrator: Orchestration = factory.get('default_orchestration')
    orchestrator.orchestrate('{}')