from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # SiliconFlow API Configuration
    SILICONFLOW_API_KEY: str
    MODEL_NAME: str = "deepseek-ai/DeepSeek-R1"
    MODEL_BASE_URL: str = "https://api.siliconflow.cn/v1"
    MODEL_TEMPERATURE: float = 0.7
    MODEL_MAX_TOKENS: int = 2048
    
    # Application Settings
    PROJECT_ROOT: Path = Path(__file__).parent.parent.parent
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()