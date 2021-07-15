from app.core.commons import Step
from app.state import factory


def step(number: int, state_class,  orchestration_name='default_orchestration', config_file=None, skippable=False):
    """
    step decorator, mark your functions with this
    """
    def outer_wrapper(func):
        orchestrator = factory.get(orchestration_name)
        if not orchestrator:
            orchestrator = factory.register(orchestration_name, state_class, config_file)

        orchestrator.steps.append(Step(number, func, skippable))

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    return outer_wrapper
