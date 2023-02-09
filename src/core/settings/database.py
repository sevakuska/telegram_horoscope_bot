from pydantic import BaseSettings


class _DatabaseSettings(BaseSettings):
    engine_type: str
    database_name: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


database_settings = _DatabaseSettings()
