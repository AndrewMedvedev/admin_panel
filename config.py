from dotenv import dotenv_values, find_dotenv

env_path = find_dotenv()


def load_config() -> dict:
    env_path = find_dotenv(".env")

    if not env_path:
        env_path = find_dotenv(".test.env")

    return dotenv_values(env_path)


config = load_config()


class Settings:
    EVENTS_ADD: str = config["EVENTS_ADD"]
    EVENTS_GET: str = config["EVENTS_GET"]
    EVENTS_DELETE: str = config["EVENTS_DELETE"]

    NEWS_ADD: str = config["NEWS_ADD"]
    NEWS_GET: str = config["NEWS_GET"]
    NEWS_DELETE: str = config["NEWS_DELETE"]


settings = Settings()
