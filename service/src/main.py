import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.api.v1.main import router as api_v1_router
from src.core.config import Settings
from src.core.logger import LOGGING

app = FastAPI(
    title=Settings.APP_NAME,
    description=Settings.APP_DESCRIPTION,
    version=Settings.APP_VERSION,
    docs_url=f"{Settings.API_V1_PREFIX}/openapi",
    openapi_url=f"{Settings.API_V1_PREFIX}/openapi.json",
    default_response_class=ORJSONResponse
)

app.include_router(api_v1_router)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=Settings.APP_PORT,
        log_config=LOGGING,
        log_level=Settings.LOG_LEVEL,
    )
