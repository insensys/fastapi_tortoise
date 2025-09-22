from celery.result import AsyncResult
from src.celery.celery import app
import asyncio
from src.services.request import get_request, get_headers, get_params, build_url


@app.task (name="fetch_invoices")
def fetch_invoices():
    """
    Task for celery. That sends req to the server
    """
    url_value=build_url()
    headers_value=get_headers()
    params_value=get_params()

    return asyncio.run(
        get_request(url=url_value, headers=headers_value, params=params_value)
    )


@app.task(name="simple_task")
def add_two_digits(x:int, y:int):
    return x+y


def get_status(task_id:str) -> AsyncResult:
    return app.AsyncResult(task_id)

def celery_task(task_id: str) -> None:
    app.control.revoke(task_id, terminate=True, signal="SIGKILL")