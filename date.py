class Date:
    def __init__(self, fulldate):
        parsed = fulldate.split("-")
        if len(parsed) < 3 or len(fulldate) != 10:
            self.year = "none"
        else:
            self.year = parsed[0]
            self.month = parsed[1]
            self.day = parsed[2]

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def equal(self, comp):
        if self.year == comp.get_year() and self.month == comp.get_month() and self.day == comp.get_day():
            return True
        return False

    def in_span(self, start, end):
        if end == "none":
            return self.equal(start)
        if self.year != start.get_year():
            return False
        if start.get_month() < self.month < end.get_month():
            return True
        elif self.month == start.get_month() :
            if self.day > start.get_day():
                return True
        elif self.month == end.get_month():
            if self.day < end.get_day():
                return True
        return False

    def __str__(self):
        return str(self.year) + "-" + str(self.month).zfill(2) + "-" + str(self.day).zfill(2)
