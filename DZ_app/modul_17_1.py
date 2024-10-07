from fastapi import FastAPI
from DZ_app.__task__ import router as task_router
from DZ_app.__user__ import router as user_router


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)