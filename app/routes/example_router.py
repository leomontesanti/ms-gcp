from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "This is an exemple endpoint for the MS"}

@router.get("/health")
def health_check():
    return {"status": "healthy"}