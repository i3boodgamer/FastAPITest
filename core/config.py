import os

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

os.path.join(os.path.dirname(__file__), '.env')

class Settings(BaseSettings):
    api_v1_prefix : str = "/api/v1"
    
    DB_URL: SecretStr
    DB_echo: bool = True
    
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf8",
    )

settings = Settings()