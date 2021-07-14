import logging
import os
from logging import handlers

from celery import Celery
from celery.signals import after_setup_logger

celery_app = Celery(
    main="tasks",
    broker=os.getenv("CELERY_BROKER_STRING", "redis://localhost:6379/0")
)

# App configurations and queue definitions

celery_app.conf.update(task_acks_late=True, task_default_queue="tasks")

celery_app.conf.task_routes = {
    "orchestration.tasks": {"queue": "orchestration"}
}


@after_setup_logger.connect
def setup_logger(logger, *args, **kwargs):
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    if not os.path.exists('logs'):
        os.mkdir('logs')

    fh = handlers.WatchedFileHandler('logs/orchestrator.log')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.setLevel('INFO')
    return logger
