from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_user: str
    database_password: str
    database_host: str
    database_port: str
    database_name: str
    api_url: str

    class Config:
        env_file = ".env"


settings = Settings()
