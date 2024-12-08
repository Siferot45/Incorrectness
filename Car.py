from IncorrectCarNumbers import IncorrectCarNumbers
from IncorrectVinNumber import IncorrectVinNumber


class Car:
    """Класс для представления автомобиля с проверкой VIN номера и госномеров."""

    def __init__(self, model, vin, numbers):
        """Инициализирует автомобиль с моделью, VIN номером и государственными номерами.

        Args:
            model (str): Модель автомобиля.
            vin (int): VIN номер автомобиля.
            numbers (str): Государственные номера автомобиля.
        """
        self.model = model

        if self.__is_valid_vin(vin):  # Проверка корректности VIN номера
            self.__vin = vin

        if self.__is_valid_numbers(numbers):  # Проверка корректности номеров
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        """Проверяет корректность VIN номера.

        Args:
            vin_number (int): VIN номер для проверки.

        Returns:
            bool: True, если VIN номер корректен.

        Raises:
            IncorrectVinNumber: Если VIN номер некорректного типа или находится вне допустимого диапазона.
        """
        if not isinstance(vin_number, int):  # Проверка типа VIN номера
            raise IncorrectVinNumber('Некорректный тип VIN номера')

        if not 1000000 <= vin_number <= 9999999:  # Проверка диапазона VIN номера
            raise IncorrectVinNumber('Неверный диапазон для VIN номера')

        return True

    def __is_valid_numbers(self, numbers):
        """Проверяет корректность государственных номеров.

        Args:
            numbers (str): Государственные номера для проверки.

        Returns:
            bool: True, если номера корректны.

        Raises:
            IncorrectCarNumbers: Если номера некорректного типа или длины.
        """
        if not isinstance(numbers, str):  # Проверка типа номеров
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

        if len(numbers) != 6:  # Проверка длины номеров
            raise IncorrectCarNumbers('Неверная длина номера')

        return True

