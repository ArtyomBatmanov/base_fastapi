from pydantic.v1 import BaseSettings
from pydantic import BaseModel
from pydantic import PostgresDsn

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool
    echo_pool: bool
    pool_size: int = 50,
    max_overflow: int = 10

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    # prefix
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


settings = Settings()
