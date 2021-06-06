"""
test apirouter
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def home():
    """
    Home endpoint
    """
    return 'hello from test'
    