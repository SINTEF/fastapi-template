"""
app init
"""
from fastapi import FastAPI
from app.routers import dummy


def create_app():
    """
    Create the FastAPI app
    """
    app = FastAPI()
    app.include_router(dummy.router)
    return app
