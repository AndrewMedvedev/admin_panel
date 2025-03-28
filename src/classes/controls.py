import logging

from src.errors import SendError

log = logging.getLogger(__name__)


async def valid_answer(
    response,
    name_func: str,
):
    try:
        log.warning(await response.text())
        if response.status == 200:
            data_dict = await response.json()
            log.warning(data_dict)
            return data_dict
        else:
            raise SendError(
                name_func=name_func,
                message="Пришли неверные данные",
            )
    except Exception:
        raise SendError(
            name_func=name_func,
            message="Ошибка отправки",
        )


def config_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M",
        format="[%(asctime)s] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )
