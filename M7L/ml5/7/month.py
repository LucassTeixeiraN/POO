class Month:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, year: int):
        self.year = year
        if self.is_leap_year(year):
            self.days_in_month[1] = 29

    def show(self, month: int):
        if not self.is_month_valid(month):
            return

        days = self.get_days(month)
        start_day = self.__get_first_day(month) + 1
        
        print(f"\nMês: {month}, Ano: {self.year}")
        print("D  S  T  Q  Q  S  S")

        for _ in range(start_day):
            print("  ", end=" ")

        for day in range(1, days + 1):
            print(f"{str(day).zfill(2)}", end=" ")
            if (day + start_day) % 7 == 0:
                print()
        print("\n")

    def __get_first_day(self, month: int):
        '''Return the day based on the Zeller's Congruence formula.'''
        if month == 1 or month == 2:
            year = self.year - 1
            month += 12
        else:
            year = self.year

        k = year % 100
        j = year // 100
        first_day = (1 + (13 * (month + 1)) // 5 + k + k // 4 + year // 400 + 5 * j) % 7
        return (first_day + 5) % 7 
    
    @classmethod
    def get_days(cls, month: int):
        return cls.days_in_month[month - 1]
    
    @staticmethod
    def is_month_valid(month: int):
        if not (1 <= month <= 12) or not isinstance(month, int):
            print("Mês inválido. Digite um valor entre 1 e 12.")
            return False
        return True
    
    @staticmethod
    def is_leap_year(year: int):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)