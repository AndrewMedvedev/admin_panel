from dotenv import dotenv_values, find_dotenv

env_path = find_dotenv()


config = dotenv_values(env_path)


class Settings:
    VALIDATE_TOKENS: str | None = config["VALIDATE_TOKENS"]

    EVENTS_ADD: str | None = config["EVENTS_ADD"]
    EVENTS_GET: str | None = config["EVENTS_GET"]
    EVENTS_DELETE: str | None = config["EVENTS_DELETE"]

    NEWS_ADD: str | None = config["NEWS_ADD"]
    NEWS_GET: str | None = config["NEWS_GET"]
    NEWS_DELETE: str | None = config["NEWS_DELETE"]


settings = Settings()
