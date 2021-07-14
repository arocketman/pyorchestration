import os
import json

from celery import Celery

if __name__ == '__main__':
    celery_app = Celery(
        main="tasks",
        broker=os.getenv("CELERY_BROKER_STRING", "redis://localhost:6379/0")
    )

    # App configurations and queue definitions

    celery_app.conf.update(task_acks_late=True, task_default_queue="tasks")

    celery_app.conf.task_routes = {
        "orchestration.tasks": {"queue": "orchestration"}
    }

    celery_app.send_task(
        "orchestration.tasks.orchestrate",
        args=[
            "default_orchestration",
            json.dumps({
                "name": "Andrea"
            })
        ]
    )
