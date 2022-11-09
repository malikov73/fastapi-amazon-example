from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


app.include_router(router, prefix="/api")

handler = Mangum(app=app)
