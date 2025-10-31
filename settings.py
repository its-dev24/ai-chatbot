from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GROQ_ENDPOINT: str
    GROQ_KEY: str
    GROQ_DEPLOYMENT: str
    API_URL: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()  # type: ignore
