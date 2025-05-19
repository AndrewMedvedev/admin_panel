import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    VALIDATE_TOKENS: str | None = os.getenv("VALIDATE_TOKENS")

    EVENTS_ADD: str | None = os.getenv("EVENTS_ADD")
    EVENTS_GET: str | None = os.getenv("EVENTS_GET")
    EVENTS_DELETE: str | None = os.getenv("EVENTS_DELETE")

    NEWS_ADD: str | None = os.getenv("NEWS_ADD")
    NEWS_GET: str | None = os.getenv("NEWS_GET")
    NEWS_DELETE: str | None = os.getenv("NEWS_DELETE")


settings = Settings()
