from month import Month

class Calendar:
    holidays = {
        "01-01": "Ano Novo",
        "21-04": "Tiradentes",
        "01-05": "Dia do Trabalho",
        "07-09": "Independência",
        "12-10": "Nossa Senhora Aparecida",
        "02-11": "Finados",
        "15-11": "Proclamação da República",
        "25-12": "Natal",
        "31-12": "Ano Novo",
    }

    def __init__(self, month: Month):
        self.month = month

    def calculate_days_between(self, date1: str, date2: str):
        day1, month1 = map(int, date1.split('-'))
        day2, month2 = map(int, date2.split('-'))

        total_days1 = self.__calculate_days_since_start(month1, day1)
        total_days2 = self.__calculate_days_since_start(month2, day2)

        return abs(total_days2 - total_days1)
    
    @classmethod
    def verifyHoliday(cls, day: int, month: int):
        date_key = f"{str(day).zfill(2)}-{str(month).zfill(2)}" # Adiciona zeros no começo dos dias
        if cls.holidays.get(date_key, False):
            return f'A data {cls.holidays[date_key]} é feriado'
        return 'A data não é feriado'

    def __calculate_days_since_start(self, month: int, day: int):
        total_days = 0

        for y in range(1, self.month.year):
            total_days += 366 if self.month.is_leap_year(y) else 365

        for m in range(1, month):
            total_days += self.month.get_days(m)

        total_days += day
        return total_days