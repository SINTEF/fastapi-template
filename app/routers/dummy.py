"""
test apirouter
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def home():
    """
    Return a simple "Hello World" message.

    Returns:
        A dictionary with a message key and "Hello World" value.
    """
    return {"msg": "Hello World"}
