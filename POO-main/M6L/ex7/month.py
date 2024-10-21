class Month:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, year: int):
        self.year = year
        if self.is_leap_year(year):
            self.days_in_month[1] = 29

    def is_leap_year(self, year: int):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def get_days(self, month: int):
        return self.days_in_month[month - 1]

    def get_first_day_of_month(self, month: int):
        if month == 1 or month == 2:
            year = self.year - 1
            month += 12
        else:
            year = self.year

        k = year % 100
        j = year // 100
        first_day = (1 + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
        return (first_day + 5) % 7 
