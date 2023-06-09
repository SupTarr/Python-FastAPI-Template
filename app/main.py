from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(post.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "Welcome to my APIs"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",
                port=settings.app_port, reload=True)
