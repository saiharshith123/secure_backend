from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app import models
from app.database import Base, engine
from app.routers import auth, users, files
from app.logger import logger

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Secure Backend API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def request_logger(
    request: Request,
    call_next
):
    logger.info(
        "%s %s",
        request.method,
        request.url.path
    )

    response = await call_next(request)

    logger.info(
        "Response status: %s",
        response.status_code
    )

    return response


@app.get("/")
def root():
    return {
        "message": "Secure Backend API is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(files.router)