import logging

from pyorchestration.core.commons import Step
from pyorchestration.state import factory


def step(number: int, state_class,  orchestration_name='default_orchestration', config_file=None, skippable=False):
    """
    step decorator, mark your functions with this to add them to an orchestration
    """
    def outer_wrapper(func):
        orchestrator = factory.get(orchestration_name)
        if not orchestrator:
            orchestrator = factory.register(orchestration_name, state_class, config_file)

        orchestrator.steps.append(Step(number, func, skippable))
        print(f'Registered new step {func.__name__} in orchestrator {orchestration_name}')

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    return outer_wrapper
