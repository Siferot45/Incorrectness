class IncorrectCarNumbers(Exception):
    """Исключение, возникающее при некорректных государственных номерах автомобиля."""

    def __init__(self, message):
        """Инициализация исключения с сообщением об ошибке.

        Args:
            message (str): Сообщение, описывающее причину исключения.
        """
        self.message = message
