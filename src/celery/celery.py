from celery import Celery

app = Celery('src', 
             broker='pyamqp://guest:guest@localhost:5672//',
             backend='redis://localhost:6379/0')

app.conf.update(result_expires=3600,)

if __name__=='__main__':
    app.start()