from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from src.core.config import Settings

router = APIRouter(prefix=Settings.API_V1_PREFIX)


@router.get(
    path='',
    summary="Handler",
    description="Test handler",
    response_description="Hi",
)
async def handler() -> ORJSONResponse:
    return ORJSONResponse({'Hi': 'Hallo'})
