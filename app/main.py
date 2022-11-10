"""."""

import os

from fastapi import FastAPI
from mangum import Mangum

from app.routes import router

STAGE = os.environ.get('STAGE')

root_path = '/' if not STAGE else f'/{STAGE}'
app = FastAPI(root_path=root_path)


app.include_router(router, prefix='/api')

handler = Mangum(app=app)
