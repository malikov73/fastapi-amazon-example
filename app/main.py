from fastapi import APIRouter, FastAPI
from mangum import Mangum

app = FastAPI(openapi_url='/openapi.json')

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


app.include_router(router, prefix="/dev/api")

handler = Mangum(app=app)
