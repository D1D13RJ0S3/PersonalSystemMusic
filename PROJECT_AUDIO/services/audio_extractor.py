from yt_dlp import YoutubeDL
from imageio_ffmpeg import get_ffmpeg_exe
import re

def is_valid_youtube_url(url: str) -> bool:
    """
    Validate if the given URL is a valid YouTube URL.

    This function checks whether the provided URL matches the typical pattern for 
    YouTube video URLs (both standard and shortened versions).

    Args:
        url (str): The URL to validate.

    Returns:
        bool: True if the URL matches the YouTube URL pattern, False otherwise.

    Example:
        >>> is_valid_youtube_url("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        True
    """
    youtube_regex = r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[a-zA-Z0-9_-]+(\S*)?$'
    return bool(re.match(youtube_regex, url))


def downloader(url: str) -> str:
    """
    Download the audio from a YouTube video and convert it to MP3 format.

    This function uses yt-dlp to download the best audio format of a YouTube video
    and converts it to MP3 using FFmpeg. The audio file is saved in the 'audio' directory 
    with the video title as the filename.

    Args:
        url (str): The YouTube URL of the video to download the audio from.

    Returns:
        str: The title of the YouTube video.

    Raises:
        Exception: If the download fails for any reason, an exception is raised.

    Example:
        >>> downloader("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        "Never Gonna Give You Up"
    """
    ffmpeg_path = get_ffmpeg_exe()

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': ffmpeg_path,
        'outtmpl': 'audio/%(title)s.%(ext)s',
        'quit': True,
        'no_warnings': True,
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return info.get('title', 'unknown title')
    except Exception as e:
        raise Exception(f"Download failed: {str(e)}")

    
            