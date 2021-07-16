# pyorchestration

pyorchestration is a celery based orchestration engine that allows to create orchestration flows through a minimal configuration.

It provides the following features:

* Automatic retries of orchestration
* Skippable steps
* Multiple orchestrations
* Injectable configurations

## General concepts

There are three main concepts:

* An **orchestration** is a sequence of functions being executed
* A **step** is a function being executed within an orchestration
* A **State** is an object being shared throughout the steps of the orchestration

## Quickstart

First, define the orchestration state, this is an object that will be shared throughout the orchestration:

You need to override the *from_dict* method to parse the incoming request payload: 
```python
from pyorchestration.core.decorators import step
from pyorchestration.core.commons import OrchestrationState
from pyorchestration.start import celery_app

class MyState(OrchestrationState):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @classmethod
    def from_dict(cls, payload):
        return cls(payload['name'])
```

Then, you simply define your orchestration using decorators:

```python
@step(number=1, state_class=MyState)
def say_hi(state: MyState):
    logging.info(f'hi {state.name}')


@step(number=2, state_class=MyState)
def say_bye(state: MyState):
    logging.info(f'bye {state.name}')
```

That's it! You can launch the celery worker with celery command:

    celery --app app.celery_app worker

to trigger an orchestration you can use standard celery approach, you need to specify two arguments:

* orchestration_name (default is: default_orchestration)
* payload object (can be blank if not needed)

```python
    celery_app.send_task(
        "orchestration.tasks.orchestrate",
        args=[
            "default_orchestration",
            json.dumps({
                "name": "Andrea"
            })
        ]
    )
```

The worker will then pick up the new task and begin the orchestration.