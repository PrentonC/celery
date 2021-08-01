from __future__ import absolute_import
from celery import Celery
app = Celery('test_celery', broker='amqp://guest:guest@broker:5672',
             backend='rpc://', include=['test_celery.tasks'])
