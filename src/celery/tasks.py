from src.celery.celery import app


@app.task
def add(x,y):
    return x+y

@app.task
def multiply(x,y):
    return x*y