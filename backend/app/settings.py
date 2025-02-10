from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = BASE_DIR / ".env"


class Settings(BaseSettings):
    API_TITLE: str = "Milady API"
    API_DESCRIPTION: str = "API for logging in to Spotify"
    API_VERSION: str = "1.0.0"

    APP_FRONTEND_URL: str
    APP_BACKEND_URL: str
    APP_CALLBACK_URL: str

    SPOTIFY_CLIENT_ID: str
    SPOTIFY_CLIENT_SECRET: str

    DATABASE_LOGIN: str = "user"
    DATABASE_PASSWORD: str = "password"
    DATABASE_NAME: str = "database"
    DATABASE_IP: str = "localhost"
    DATABASE_PORT: int = 5432

    model_config = SettingsConfigDict(env_file=ENV_FILE)

    @property
    def SPOTIFY_AUTH_URL(self) -> str:
        return "https://accounts.spotify.com/authorize"

    @property
    def SPOTIFY_TOKEN_URL(self) -> str:
        return "https://accounts.spotify.com/api/token"

    @property
    def REDIRECT_URI(self) -> str:
        return f"{self.APP_BACKEND_URL}/api/auth/twitch/callback"

    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DATABASE_LOGIN}:{self.DATABASE_PASSWORD}@{self.DATABASE_IP}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"


settings = Settings()
database_url = settings.DB_URL
