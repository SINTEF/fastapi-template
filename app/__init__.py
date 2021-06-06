"""
app init
"""
from fastapi import FastAPI
from app.dummyapp.test import router
from app.dummyapp import test


def create_app():
    """
    Create the FastAPI app
    """
    app = FastAPI()
    app.include_router(router)
    return app
