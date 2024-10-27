from date import Date
class FormattedDate(Date):
    def __init__(self, dia, mes, ano, format_string):
        super().__init__(dia, mes, ano)
        self.format_string = format_string

    def __str__(self):
        return self.format_string.format(self.dia, self.mes, self.ano)

s