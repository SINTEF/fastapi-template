"""
Creating the FastAPI application
"""
from fastapi import FastAPI
from app.routers.dummy import router as dummy_router
from app import __version__


def create_app():
    """
    Create the FastAPI app and include a dummy router.

    Returns:
        A FastAPI app with a dummy router included.
    """
    app = FastAPI(
        title="FASTAPI-TEMPLATE",
        version=__version__,
        description="Start your project here",
    )

    app.include_router(dummy_router)
    return app


APP = create_app()
