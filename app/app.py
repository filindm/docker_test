import os
from flask import Flask
from celery import Celery


CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')

app = Flask(__name__)

celery = Celery('app', backend=CELERY_RESULT_BACKEND, broker=CELERY_BROKER_URL)
TaskBase = celery.Task
class ContextTask(TaskBase):
    abstract = True
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return TaskBase.__call__(self, *args, **kwargs)
celery.Task = ContextTask


@celery.task()
def hello(s):
    msg = 'Hello,', s
    return msg


@app.route('/')
def hello_world():
    hello.delay('world')
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
  