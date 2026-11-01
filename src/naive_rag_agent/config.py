import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    service_name: str = os.getenv("SERVICE_NAME", "naive-rag-agent")
    version: str = os.getenv("SERVICE_VERSION", "0.1.0")


settings = Settings()
