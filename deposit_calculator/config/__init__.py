import os
from pathlib import Path

from .settings import SiteSettings, ApplicationSettings

base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logs_dir = Path(base_dir) / "logs"
logs_dir.mkdir(exist_ok=True)


app_config: dict = ApplicationSettings().model_dump()
site_config: dict = SiteSettings().model_dump()
