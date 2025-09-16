from celery import Celery


app = Celery('celery_first_steps', 
             backend='redis://localhost:6379/0', broker='pyamqp://guest:guest@localhost:5672//')

@app.task
def add(x,y):
    return x+y