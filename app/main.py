"""."""
import os

from fastapi import APIRouter, FastAPI
from mangum import Mangum

STAGE = os.environ.get('STAGE')

root_path = '/' if not STAGE else f'/{STAGE}'
app = FastAPI(root_path=root_path)

router = APIRouter()


@router.get('/hi')
def get_hello_world():
    return {'result': 'Hello World'}


@router.post('/test')
def post_hello_world(name: str):
    return {
        'result': f'Hello {name}',
    }


app.include_router(router, prefix='/api')

handler = Mangum(app=app)
