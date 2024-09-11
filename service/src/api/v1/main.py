from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from src.core.config import settings

router = APIRouter(prefix=settings.api_v1_prefix)


@router.get(
    path="",
    summary="Handler",
    description="Test handler",
    response_description="Hi",
)
async def handler() -> ORJSONResponse:
    return ORJSONResponse({"Hi": "Hallo"})
