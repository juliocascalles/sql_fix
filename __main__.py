import uvicorn
from route.app import create_app


uvicorn.run(
    create_app()
)
