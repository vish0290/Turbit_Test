from fastapi import FastAPI

from routes import router

app = FastAPI(
    title="User post comment API",
    description="The CRUD operations for a simple user management system",
)


@app.get('/', tags=["Health Check"])
def basic():
    return {'message': 'Hello World'}


app.include_router(router)
