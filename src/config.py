from dotenv import dotenv_values, find_dotenv

env_path = find_dotenv()


config = dotenv_values(env_path)


class Settings:

    EVENTS_ADD: str = config["EVENTS_ADD"]
    EVENTS_GET: str = config["EVENTS_GET"]
    EVENTS_DELETE: str = config["EVENTS_DELETE"]

