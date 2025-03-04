from pydantic_settings import BaseSettings, SettingsConfigDict


class AdvancedSettings(BaseSettings):
    model_config = SettingsConfigDict(extra='ignore')
