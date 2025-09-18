from fastapi import APIRouter
from src.services.request import get_request, get_params, get_headers, build_url


invoice_router=APIRouter()

@invoice_router.get("/get_invoices")
async def get_invoices():
    result=await get_request(url=build_url(), headers=get_headers(), params=get_params())
    return result