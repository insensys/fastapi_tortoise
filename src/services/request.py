import httpx
from src.config.tunduk_config import tunduk_configs
from src.config.app_constants import TundukApi 


def get_headers():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {tunduk_configs.get_gns_token}",
        "USER-TIN": tunduk_configs.get_user_tin,
        "ClientUUID": tunduk_configs.get_client_uuid,
        "X-Road-Client": tunduk_configs.get_x_road_client,
    }
    return headers

def build_url() -> str:
    return (tunduk_configs.get_tunduk_url+TundukApi.GetRealizationInvoice.value)

def get_params() -> dict[str, str]:
    return {"contractorTin": "11608199100455"}

async def get_request(url, headers, params=None):
    """Выполнение GET запроса"""
    async with httpx.AsyncClient() as client:
        response = await client.get(url=url, headers=headers, params=params, timeout=None)
        response.raise_for_status()
        return response.json()