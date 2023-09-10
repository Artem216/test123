from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_user: str = Field(..., env="POSTGRES_USER")
    postgres_password: str = Field(..., env="POSTGRES_PASSWORD")
    postgres_host: str = Field("localhost", env="POSTGRES_HOST")
    postgres_port_number: int = Field(5432, env="POSTGRES_PORT_NUMBER")
    postgres_db: str = Field(..., env="POSTGRES_DB")


settings = Settings(_env_file=".env")