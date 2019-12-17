from date import Date
from aqi import AQI


# edits idiotic csv file
def fixline(line):
    new = []
    for i in range(1, len(line), 2):
        new.append(line[i])
    final = "".join(new)
    return final[1:].split(";")


def single_sensor(id, start, end="none"):
    measures = {"O3": 0, "NO2": 0, "SO2": 0, "PM10": 0}
    count = 0
    with open("data_10sensors_1year.csv", "rt") as data:
        reader = data.readlines()
        # Breaks up stupid ass csv
        real = []
        for i in range(2, len(reader)-1, 2):
            real = fixline(reader[i])
            # checks id
            if real[1] == id:
                curr = Date(real[0].split("T")[0])
                # checks time span
                if curr.in_span(start, end):
                    count += 1
                    # adds value to correct measurement
                    measures[real[2]] += float(real[3])
            real.clear()
        if count == 0:
            return "There were no results..."
        else:
            for key in measures:
                measures[key] /= count/4.0*20.0  # Calculates per hour value

            # Creates AQI Object and returns minimum AQI rating
            reading = AQI(measures["O3"], measures["NO2"], measures["SO2"], measures["PM10"])
            return reading.calculate()

