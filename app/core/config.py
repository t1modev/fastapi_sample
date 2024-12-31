from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    APP_NAME: str = "api_setup"
    DEBUG: bool = True
    DB_URL_SYNC: str
    DB_URL_ASYNC: str

    TELEGRAM_BOT_TOKEN: str

    class Config:
        env_file = "..env"


config = AppConfig()