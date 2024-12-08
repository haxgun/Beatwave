from os import environ
from pathlib import Path
from dotenv import load_dotenv


def str_to_bool(value: str) -> bool:
    return value.lower() in ("true", "1", "yes")

BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

dotenv_file: Path = BASE_DIR / ".env"
if dotenv_file.is_file():
    load_dotenv(dotenv_file)

SPOTIFY_CLIENT_ID = environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = environ.get("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = environ.get("REDIRECT_URI")
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"

API_TITLE = environ.get("API_TITLE", "Milady API")
API_DESCRIPTION = environ.get("API_DESCRIPTION", "API for logging in to Spotify")
API_VERSION = environ.get("API_VERSION", "1.0.0")

