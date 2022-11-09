from fastapi import APIRouter, FastAPI
from mangum import Mangum
app = FastAPI()

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


app.include_router(router, prefix="/api")

handler = Mangum(app=app)
