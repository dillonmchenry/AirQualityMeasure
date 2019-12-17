
class AQI:

    def __init__(self, o3, no2, so2, pm10):
        self.o3 = o3
        self.no2 = no2
        self.so2 = so2
        self.pm10 = pm10

    def calculate(self):
        self.o3_or_so2("o3")
        self.o3_or_so2("so2")
        self.no2_or_pm10("no2")
        self.no2_or_pm10("pm10")
        measures = [self.o3, self.no2, self.so2, self.pm10]

        return min(measures)

    def o3_or_so2(self, selection):
        val = 0.0
        if selection == "o3":
            val = self.o3
        else:
            val = self.so2

        if val <= 15.0:
            val = 10
        elif val <= 30.0:
            val = 9
        elif val <= 40.0:
            val = 8
        elif val <= 60.0:
            val = 7
        elif val <= 80.0:
            val = 6
        elif val <= 100.0:
            val = 5
        elif val <= 140.0:
            val = 4
        elif val <= 180.0:
            val = 3
        elif val <= 200.0:
            val = 2
        elif val <= 240.0:
            val = 1
        else:
            val = 0

        if selection == "o3":
            self.o3 = val
        else:
            self.so2 = val

    def no2_or_pm10(self, selection):
        val = 0.0
        if selection == "no2":
            val = self.no2
        else:
            val = self.pm10

        if val <= 10.0:
            val = 10
        elif val <= 20.0:
            val = 9
        elif val <= 30.0:
            val = 8
        elif val <= 45.0:
            val = 7
        elif val <= 60.0:
            val = 6
        elif val <= 75.0:
            val = 5
        elif val <= 100.0:
            val = 4
        elif val <= 125.0:
            val = 3
        elif val <= 150.0:
            val = 2
        elif val <= 200.0:
            val = 1
        else:
            val = 0

        if selection == "no2":
            self.no2 = val
        else:
            self.pm10 = val



