import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "slack_github_deploy.settings")

app = Celery('slack_github_deploy')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
