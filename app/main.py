from fastapi import APIRouter, FastAPI

app = FastAPI()

router = APIRouter()


@router.get("/test/")
def hello_world():
    return {
        'result': 'Hello World'
    }


app.include_router(router, prefix="/api")
