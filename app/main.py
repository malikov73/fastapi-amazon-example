from fastapi import APIRouter, FastAPI
from mangum import Mangum

app = FastAPI(openapi_url='/dev/openapi.json', root_path='/dev')

router = APIRouter()


@router.get("/test")
def hello_world():
    return {
        'result': 'Hello World'
    }


@router.post("/test")
def hello_world():
    return {
        'result': 'Hello World'
    }


app.include_router(router, prefix="/api")

handler = Mangum(app=app, api_gateway_base_path='/dev')
