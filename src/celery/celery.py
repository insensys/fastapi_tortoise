from celery import Celery

app = Celery('src', 
             broker='amqp://guest:guest@rabbitmq:5672//',
             backend='redis://redis:6379/0',
             include=['src.celery.tasks'],)

app.conf.update(result_expires=3600,)

app.conf.

if __name__=='__main__':
    app.start()