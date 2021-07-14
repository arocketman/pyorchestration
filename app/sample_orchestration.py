from app.state import factory
from app.start import celery_app


@celery_app.task(name="orchestration.tasks.orchestrate")
def orchestrate_task(orchestration_name, payload):
    factory.get(orchestration_name).orchestrate(payload)
