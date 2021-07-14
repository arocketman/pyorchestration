from app.core.commons import Step
from app.state import factory


def step(number: int, state_class,  orchestration_name='default_orchestration'):
    """
    step decorator, mark your functions with this
    """
    def outer_wrapper(func):
        factory.get(orchestration_name, state_class).steps.append(Step(number, func))

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    return outer_wrapper
