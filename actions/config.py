from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    gpt_model: str

    class Config:
        env_file = ".env"

settings = Settings()
