from fastapi import APIRouter, FastAPI
from mangum import Mangum
import os
STAGE = os.environ.get('STAGE')

root_path = '/' if not STAGE else f'/{STAGE}'
app = FastAPI(root_path=root_path)

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

handler = Mangum(app=app)
