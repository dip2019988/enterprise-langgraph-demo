import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path if env_path.exists() else None)


class Settings:
    PROJECT_NAME: str = "Enterprise Smart Incident Resolution Agent"
    VERSION: str = "5.0.0"

    # Logging Settings

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # OpenAI Settings
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL_NAME: str = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.1"))

    # LangSmith Settings
    LANGCHAIN_TRACING_V2: str = os.getenv("LANGCHAIN_TRACING_V2", "true")
    LANGCHAIN_API_KEY: str = os.getenv("LANGCHAIN_API_KEY", "")
    LANGCHAIN_PROJECT: str = os.getenv("LANGCHAIN_PROJECT", "Enterprise-Incident-Resolution-Agent")

    # Operational Limits
    MAX_RETRY_COUNT: int = 2
    CONFIDENCE_THRESHOLD: int = 70

    # Redis Settings
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379"))
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD", "")
    REDIS_CACHE_TTL: int = int(os.getenv("REDIS_CACHE_TTL", "3600"))

    # Mem0 Settings
    MEM0_API_KEY: str = os.getenv("MEM0_API_KEY", "")

    # MCP Endpoints
    MCP_MONITORING_URL: str = os.getenv("MCP_MONITORING_URL", "http://localhost:8001")
    MCP_GITHUB_URL: str = os.getenv("MCP_GITHUB_URL", "http://localhost:8002")
    MCP_BILLING_URL: str = os.getenv("MCP_BILLING_URL", "http://localhost:8003")

    # JWT Security
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "super-secret-enterprise-jwt-key")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 8

    # Paths
    DATA_DIR: Path = BASE_DIR / "data"
    KB_FILE_PATH: Path = DATA_DIR / "kb.json"

    @classmethod
    def validate(cls) -> None:
        if not cls.OPENAI_API_KEY or cls.OPENAI_API_KEY == "your_openai_api_key_here":
            raise ValueError("CRITICAL: OPENAI_API_KEY is not set.")


settings = Settings()
