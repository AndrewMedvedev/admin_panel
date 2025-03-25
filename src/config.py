from dotenv import dotenv_values, find_dotenv

env_path = find_dotenv()


config = dotenv_values(env_path)


class Settings:

    EVENTS_ADD: str = config["EVENTS_ADD"]
    EVENTS_GET: str = config["EVENTS_GET"]
    EVENTS_DELETE: str = config["EVENTS_DELETE"]

    USERS: str = config["USERS"]
    USERS_COUNT: str = config["USERS_COUNT"]
    USERS_PER_DAY_COUNT: str = config["USERS_PER_DAY_COUNT"]
    USERS_USER_ID: str = config["USERS_USER_ID"]

    USERS_W_S_C_CONTACTS: str = config["USERS_W_S_C_CONTACTS"]
    USERS_W_S_C_COUNT: str = config["USERS_W_S_C_COUNT"]
    USERS_W_S_C_PER_DAY_COUNT: str = config["USERS_W_S_C_PER_DAY_COUNT"]
    USERS_W_S_C_USER_ID: str = config["USERS_W_S_C_USER_ID"]

    CHATS_HISTORY: str = config["CHATS_HISTORY"]
    CHATS_HISTORY_COUNT: str = config["CHATS_HISTORY_COUNT"]
    CHATS_HISTORY_PER_DAY_COUNT: str = config["CHATS_HISTORY_PER_DAY_COUNT"]
    CHATS_HISTORY_USER_ID: str = config["CHATS_HISTORY_USER_ID"]
    CHATS_HISTORY_USER_ID_COUNT: str = config["CHATS_HISTORY_USER_ID_COUNT"]

    NOTIFICATIONS_ALL: str = config["NOTIFICATIONS_ALL"]
    NOTIFICATIONS_BY_PHONE_NUMBER: str = config["NOTIFICATIONS_BY_PHONE_NUMBER"]
