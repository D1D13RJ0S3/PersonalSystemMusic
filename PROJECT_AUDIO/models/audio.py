from pydantic import BaseModel

class AudioUrl(BaseModel):
    """
    Model for representing the YouTube URL of a video to be downloaded as audio.

    This model is used to validate the input data for the URL of the YouTube video 
    that the user wants to download the audio from. The URL is provided as a string.

    Attributes:
        url (str): The YouTube URL of the video to be downloaded.

    Example:
        {
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        }
    """
    url: str

