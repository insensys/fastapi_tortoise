
from starlette.status import HTTP_307_TEMPORARY_REDIRECT
from src.celery.celery import app as celery_app
from fastapi import APIRouter
from src.services.request import get_request, get_params, get_headers, build_url
from src.celery.tasks import fetch_invoices, add_two_digits
from kombu.exceptions import OperationalError as KombuOperationalError
from fastapi import HTTPException
from celery.result import AsyncResult



invoice_router=APIRouter()

@invoice_router.get("/get_invoices")
async def get_invoices():
    result=await get_request(url=build_url(), headers=get_headers(), params=get_params())
    return result

@invoice_router.get("/task_get_invoices")
def task_get_invoices_async():
    # try:
    #     task = fetch_invoices.delay()
    #     return {"task id": task.id, "status": "PENDING"}
    # except KombuOperationalError as e:
    #     raise HTTPException (status_code=503, detail=f"Message broker in not available, maybe probles with VPN: {e}")
    # except Exception as e:
    #     raise HTTPException(status_code=505, detail=str(e))

    resp = fetch_invoices.delay()
    
    print (resp.status)
    print (f"resp.ready: {resp.ready}")
    print (resp.result)
    return {"task_id": resp.id, "status": "PENDING"}
    
@invoice_router.get("/tasks_status/{task_id}")
def task_status(task_id: str):
    """Checking task status/results"""

    task_result = AsyncResult(task_id, app = celery_app)

    if task_result.state == 'PENDING':
        response={
            "state": task_result.state,
            "status": "Pending..."
        }
    elif task_result.state != "FAILURE":
        response = {
            "state": task_result.state,
            "status": task_result.info
        }
    else:
        response = {
            "state": task_result.state,
            "status": str(task_result.info)
        }
    return response


@invoice_router.get(f"/simple_task")
async def run_simple_task(x,y):
    try:
        task = add_two_digits.delay(x,y)
        return {"task_id": task.id, "status": "PENDING"}
    except KombuOperationalError as e:
        raise HTTPException(status_code=503, detail=f"Message broker is unavsilable: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@invoice_router.get("/simple_task_result/{task_id}")
def simple_task_result(task_id:str):
    res = celery_app.AsyncResult(task_id)
    if not res.ready():
        return {"task_id": task_id, "state": res.state, "status": "PENDING"}
    if res.failed():
        return {"task_id": task_id, "state": res.state, "error": str(res.result)}
    
    return {"task_if": task_id, "state": res.state, "result": res.result}


# @app.get("/task-status/{task_id}")
# def task_status(task_id: str):
#     task_result = AsyncResult(task_id, app=celery_worker.celery)
#     if task_result.state == 'PENDING':
#         response = {
#             "state": task_result.state,
#             "status": "Pending..."
#         }
#     elif task_result.state != 'FAILURE':
#         response = {
#             "state": task_result.state,
#             "status": task_result.info
#         }
#     else:
#         response = {
#             "state": task_result.state,
#             "status": str(task_result.info)
#         }
#     return response