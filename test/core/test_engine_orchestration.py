import pytest

from app.core.decorators import step
from app.core.engine import Orchestration
from app.core.exceptions import IllegalOrchestrationGraphException
from app.state import factory
from test.fixtures import TestState


@step(1, state_class=TestState, orchestration_name='ok_orchestration')
def correct_step(state_object: TestState):
    state_object.name = 'hello_test'


@step(2, state_class=TestState, orchestration_name='ok_orchestration', skippable=True)
def wrong_skippable_step(state_object: TestState):
    # Forcing an exception
    state_object.age = 100 / 0


@step(3, state_class=TestState, orchestration_name='ok_orchestration', skippable=True)
def another_correct_step(state_object: TestState):
    state_object.age = 5


@step(1, state_class=TestState, orchestration_name='cfg_orchestration', config_file='test/resources/example_cfg.yml')
def cfg_step(state_object: TestState):
    pass


def test_orchestration_execution():
    orchestrator: Orchestration = factory.get('ok_orchestration')
    final_state = orchestrator.orchestrate('{}')
    assert final_state.name == 'hello_test'
    assert final_state.age == 5


def test_same_step_number():
    with pytest.raises(IllegalOrchestrationGraphException):
        @step(1, state_class=TestState, orchestration_name='test')
        def x(state_object: TestState):
            state_object.name = 'hello_test_x'

        @step(1, state_class=TestState, orchestration_name='test')
        def y(state_object: TestState):
            state_object.name = 'hello_test_y'

        factory.get('test').orchestrate('{}')


def test_read_orchestration():
    orchestrator: Orchestration = factory.get('cfg_orchestration')
    final_state = orchestrator.orchestrate('{}')
    assert final_state.cfg.get('name') == 'Andrea'
    assert final_state.cfg.get('username') == 'arocketman'
    assert final_state.cfg['test']['foo'] == 'bar'

