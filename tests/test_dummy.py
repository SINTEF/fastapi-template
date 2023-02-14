from fastapi import APIRouter
import pytest

@pytest.fixture
def router():
    return APIRouter()

def test_home(router):
     @router.get("/")
     async def home():
        response = await home()
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}
