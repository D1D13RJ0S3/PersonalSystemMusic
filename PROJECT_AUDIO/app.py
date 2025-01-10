from fastapi import FastAPI, HTTPException
from services.audio_extractor import is_valid_youtube_url, downloader
from urllib.parse import unquote
from pydantic import BaseModel
from routes.audio import router

app = FastAPI(
    title="Youtube Audio Downloader",
    description="API for downloading YouTube videos as MP3 files",
    version="1.0.0"
)

@app.on_event("startup")
async def startup():
    """
    This function is executed when the FastAPI application starts.

    It can be used for any initialization tasks like database connections or 
    preparing services. Currently, no specific startup tasks are configured.
    """
    pass

@app.on_event("shutdown")
async def shutdown():
    """
    This function is executed when the FastAPI application shuts down.

    It can be used for cleanup tasks such as closing database connections or 
    shutting down services. Currently, no specific shutdown tasks are configured.
    """
    pass

# Include the router for the audio download functionality
app.include_router(router)



    