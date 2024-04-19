print('Задача 3. Дата')

# Реализуйте класс Date, который должен:
#
# проверять числа даты на корректность;
# конвертировать строку даты в объект класса Date, состоящий из соответствующих числовых значений дня, месяца и года.
# Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.
#
# При тестировании программы объект класса Date должен инициализироваться исключительно через метод конвертации


class Date:

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

    @property
    def day(self) -> int:
        return self._day

    @property
    def month(self) -> int:
        return self._month

    @property
    def year(self) -> int:
        return self._year

    @classmethod
    def from_string(cls, date_str: str) -> 'Date':
        try:
            day, month, year = map(int, date_str.split('-'))
            if not cls.is_date_valid(date_str):
                raise ValueError("Невалидная дата.")
            return cls(day, month, year)
        except ValueError as e:
            raise ValueError(f"Ошибка при создании даты из строки: {e}")

    @staticmethod
    def is_date_valid(date_str: str) -> bool:
        try:
            day, month, year = map(int, date_str.split('-'))
            return 1 <= day <= 31 and 1 <= month <= 12
        except ValueError:
            return False

    def __str__(self) -> str:
        return f"День: {self._day}\tМесяц: {self._month}\tГод: {self._year}"


try:
    date = Date.from_string('10-12-2077')
    print(date)
except ValueError as e:
    print(e)

print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

print()
