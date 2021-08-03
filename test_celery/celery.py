from __future__ import absolute_import
from celery import Celery
from kombu import Exchange, Queue

app = Celery('test_celery', broker='amqp://guest:guest@broker:5672',
             backend='rpc://', include=['test_celery.tasks'])

app.conf.task_default_queue = 'default'
app.conf.task_queues = (
    Queue('default', routing_key='default'),
    Queue('slow_tasks', routing_key='exchange1.slow_tasks'),
)
app.conf.task_default_exchange = 'tasks'
app.conf.task_default_exchange_type = 'direct'
app.conf.task_default_routing_key = 'default'
