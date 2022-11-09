from fastapi import APIRouter, FastAPI
from mangum import Mangum
from pydantic import BaseSettings


class Settings(BaseSettings):
    openapi_url: str = "/dev/openapi.json"


settings = Settings()

app = FastAPI(openapi_url=settings.openapi_url)

router = APIRouter()


@router.get("/test/")
def hello_world():
    return {
        'result': 'Hello World'
    }


@router.post("/test/")
def hello_world():
    return {
        'result': 'Hello World'
    }


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


app.include_router(router, prefix="/api")

handler = Mangum(app=app)
