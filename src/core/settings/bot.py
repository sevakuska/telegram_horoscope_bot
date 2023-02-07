from pydantic import BaseSettings
from pydantic import SecretStr


class _BotSettings(BaseSettings):
    bot_token: SecretStr

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


bot_settings = _BotSettings()
