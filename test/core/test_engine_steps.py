import pytest

from test.fixtures import TestState
from app.core.decorators import step
from app.core.engine import Orchestration
from app.state import factory


@step(1, state_class=TestState, orchestration_name='ok_orchestration_1')
def correct_step(state_object: TestState):
    state_object.name = 'hello_test'


@step(1, state_class=TestState, orchestration_name='skippable_orchestration', skippable=True)
def wrong_skippable_step(state_object: TestState):
    # Forcing an exception
    state_object.age = 100/0


@step(1, state_class=TestState, orchestration_name='bad_orchestration')
def wrong_step(state_object: TestState):
    # Forcing an exception
    state_object.age = 100/0


def test_execute_correct_step():
    orchestrator: Orchestration = factory.get('ok_orchestration_1')
    final_state = orchestrator.orchestrate('{}')
    assert final_state.name == 'hello_test'


def test_skippable_step():
    orchestrator: Orchestration = factory.get('skippable_orchestration')
    orchestrator.orchestrate('{}')


def test_execute_wrong_step():
    with pytest.raises(Exception):
        orchestrator: Orchestration = factory.get('bad_orchestration')
        orchestrator.orchestrate('{}')

