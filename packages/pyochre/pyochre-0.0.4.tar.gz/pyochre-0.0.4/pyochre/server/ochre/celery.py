import os
import logging
from celery import Celery


logger = logging.getLogger(__name__)


os.environ.setdefault("USE_CELERY", "True")


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'pyochre.server.ochre.settings'
)


app = Celery('ochre')


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    logger.debug(f'Request: {self.request!r}')    
