from pydantic import Field

from .base import AdvancedSettings


class ApplicationSettings(AdvancedSettings):
    title: str = Field("Deposit calculation service", alias="APP_NAME")
    description: str = Field("Deposit calculation service")
    openapi_url: str = Field("/openapi.json")
    debug: bool = Field(True, alias="DEBUG")
    version: str = Field("0.1.0", alias="APP_VERSION")


class SiteSettings(AdvancedSettings):
    host: str = Field("127.0.0.1", alias="SITE_HOST")
    port: int = Field(8000, alias="SITE_PORT")
    log_level: str = Field("info", alias="SITE_LOG_LEVEL")
    reload: bool = Field(True, alias="SITE_RELOAD")
    reload_delay: float = Field(0.25, alias="SITE_RELOAD_DELAY")
