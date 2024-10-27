from month import Month
from typing import Callable

class Calendar:
    def __init__(self, year: int):
        self.month = Month(year)

    def calculate_days_between(self, date1: str, date2: str):
        day1, month1 = map(int, date1.split('-'))
        day2, month2 = map(int, date2.split('-'))

        total_days1 = self.__calculate_days_since_start(month1, day1)
        total_days2 = self.__calculate_days_since_start(month2, day2)

        return abs(total_days2 - total_days1)
    
    @classmethod
    def verifyHoliday(cls, day: int, month: int, function: Callable):
        return function(day, month)

    def __calculate_days_since_start(self, month: int, day: int):
        total_days = 0

        for y in range(1, self.month.year):
            total_days += 366 if self.month.is_leap_year(y) else 365

        for m in range(1, month):
            total_days += self.month.get_days(m)

        total_days += day
        return total_days