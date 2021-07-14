from sample_orchestration import MyState
from app.core.decorators import step


@step(number=1, state_class=MyState)
def step_one(state: MyState):
    state.age = 5
    print('one')

@step(number=2, state_class=MyState)
def step_two(state: MyState):
    print(state.age)
    print('two')

@step(number=3, state_class=MyState)
def print_all(state: MyState):
    print(state.name)
    print(state.age)

