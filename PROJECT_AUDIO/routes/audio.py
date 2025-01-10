from fastapi import APIRouter, HTTPException
from services.audio_extractor import is_valid_youtube_url, downloader
from urllib.parse import unquote
from models.audio import AudioUrl

# Create a router to handle routes related to audio downloading
router = APIRouter()

@router.post("/download/")
async def download(url: AudioUrl):
    """
    Download the audio from a YouTube video and return the title of the downloaded video.

    This function receives a YouTube URL, validates it, and if valid, proceeds to download 
    the audio from the video as an MP3 file. If the URL is invalid or the video cannot be processed, 
    an appropriate HTTP error is returned.

    Args:
        url (AudioUrl): An object containing the YouTube URL of the video to download.

    Returns:
        dict: A response with the status of the operation and the title of the downloaded video.

    Raises:
        HTTPException: If the provided URL is invalid or an internal error occurs.
    """
    try:
        # Decode the URL to properly handle special characters
        decoded_url = unquote(url.url)
        
        # Validate that the URL starts with "http"
        if not decoded_url.startswith("http"):
            raise HTTPException(status_code=400, detail="Invalid URL")
        
        # Validate if the URL is a valid YouTube URL
        if not is_valid_youtube_url(decoded_url):
            raise HTTPException(status_code=400, detail="Invalid YouTube URL")
        
        # Download the audio from the YouTube video
        title = downloader(decoded_url)
        
        # Return a successful response with the title of the downloaded video
        return {
            "status": "success",
            "message": f"Downloaded {title}",
            "title": title
        }
        
    except HTTPException as he:
        # Re-raise HTTP exceptions for specific errors
        raise he
    except Exception as e:
        # Re-raise a generic HTTP exception for other unexpected errors
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

