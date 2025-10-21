from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Modular App"
    ENV: str = "development"

settings = Settings()
