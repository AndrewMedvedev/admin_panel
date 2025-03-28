class SendError(Exception):

    def __init__(
        self,
        name_func: str,
        message: str,
    ) -> None:
        self.name_func = name_func
        self.message = message
        super().__init__(
            self.name_func,
            self.message,
        )

    def __str__(self) -> str:
        return f"Ошибка в функции {self.name_func}, {self.message}."
