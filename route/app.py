from fastapi import FastAPI
from route  import transform
from route import two_queries


def create_app():
    app = FastAPI()
    app.include_router(transform.router,   tags=['transform'])
    app.include_router(two_queries.router, tags=['two_queries'])
    return app
