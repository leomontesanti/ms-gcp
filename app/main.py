from fastapi import FastAPI, APIRouter
from app.routes.example_router import router as example_router

app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)

v1_router = APIRouter()
v1_router.include_router(example_router, tags=["example"])

app.include_router(v1_router, prefix="/v1")