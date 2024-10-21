class BrHolidays:
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
    
    @classmethod
    def verifyHoliday(cls, day: int, month: int):
        date_key = f"{str(day).zfill(2)}-{str(month).zfill(2)}"
        if cls.holidays.get(date_key, False):
            return f'A data {cls.holidays[date_key]} é feriado'
        return 'A data não é feriado'