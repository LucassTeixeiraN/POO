class Calendar:
    holidays = {
            "01-01": "Ano Novo",
            "21-04": "Tiradentes",
            "07-09": "Independencia",
            "25-12": "Natal",
        }
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def __init__(self, year: int):
        self.year = year

        if self.isLeapYear(self.year):
            self.days_in_month[1] = 29

    def isLeapYear(self, year: int): #Retorna se é ano bissexto
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def showMonth(self, month: int):
        if not (1 <= month <= 12):
            print("Mês inválido. Digite um valor entre 1 e 12.")
            return

        days = self.days_in_month[month - 1]
        print(f"\nMês: {month}, Ano: {self.year}")
        print("D S T Q Q S S")

        start_day = self.__getFirstDayOfMonth(month)
        day = 1

        for _ in range(start_day):
            print("  ", end=" ")

        for day in range(1, days + 1):
            print(f"{str(day).zfill(2)}", end=" ") # Adiciona zeros no começo dos dias
            if (day + start_day) % 7 == 0:
                print()
        print("\n") 

    def __getFirstDayOfMonth(self, month: int):
        if month == 1 or month == 2:
            year = self.year - 1
            month += 12
        else:
            year = self.year

        k = year % 100
        j = year // 100
        first_day = (1 + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
        return (first_day + 5) % 7 

    def verifyHoliday(self, day: int, month: int):
        date_key = f"{str(day).zfill(2)}-{str(month).zfill(2)}" # Adiciona zeros no começo dos dias
        return self.holidays.get(date_key, "Não é feriado")

    def calculateDaysBetween(self, date1: str, date2: str):
        day1, month1, year1 = map(int, date1.split('-'))
        day2, month2, year2 = map(int, date2.split('-'))

        total_days1 = self.__calculateDaysSinceStart(year1, month1, day1)
        total_days2 = self.__calculateDaysSinceStart(year2, month2, day2)

        return abs(total_days2 - total_days1)

    def __calculateDaysSinceStart(self, year: int, month: int, day: int):
        total_days = 0

        for y in range(1, year):
            total_days += 366 if self.isLeapYear(y) else 365

        for m in range(1, month):
            total_days += self.days_in_month[m - 1]

        total_days += day
        return total_days