class UsHolidays:
    holidays = {
        "01-01": "New Year's Day",
        "01-15": "Martin Luther King Jr. Day",
        "02-19": "Presidents' Day",
        "05-27": "Memorial Day",
        "07-04": "Independence Day",
        "09-02": "Labor Day",
        "10-14": "Columbus Day",
        "11-11": "Veterans Day",
        "11-28": "Thanksgiving",
        "12-25": "Christmas",
    }
    
    @classmethod
    def verifyHoliday(cls, day: int, month: int):
        date_key = f"{str(month).zfill(2)}-{str(day).zfill(2)}"
        if cls.holidays.get(date_key, False):
            return f'"{cls.holidays[date_key]}" is a holiday'
        return 'The date is not a holiday'