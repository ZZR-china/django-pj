from celery import Celery

app = Celery('test_celery',
             broker='redis://localhost:6379//0',
             backend='redis',
             include=['test_celery.tasks'])
