import csv,sys
from sensor import Sensor
from date import Date
# List of sensors
sensors = []

# Square location range
lat_min = 0.0
lat_max = 70.0
long_min = -40.0
long_max = 100.0

# Circular location range
lat = 0.0
long = 0.0
radius = 0.0

# date


def single_sensor(id, start, end):
    with open("data_10sensors_1year.csv", "rt") as data:
        reader = data.readlines()
        # Breaks up stupid ass csv
        real = []
        for i in range(2, len(reader)-1, 2):
            real = fixline(reader[i])
            if real[1] == id:
                curr = Date(real[0].split("T")[0])
                if curr.in_span(start, end):
                    print("Gather value")
            real.clear()


def fixline(line):
    new = []
    for i in range(1, len(line), 2):
        new.append(line[i])
    final = "".join(new)
    return final.split(";")


# Tests if lat long is in range of given parameters
def in_range(loc, area_type):
    if lat_min <= loc[0] <= lat_max and long_min <= loc[1] <= long_max:
        return True
    else:
        return False


# Collects all sensors in list
with open("sensors.csv", "rt") as f:
    entries = csv.DictReader(f, fieldnames=None, delimiter=";", quoting=csv.QUOTE_ALL)
    for row in entries:
        sensors.append(Sensor(row["SensorID"], float(row["Latitude"]), float(row["Longitude"])))


#Menu Flow
print("Welcome to The Air Quality Management System!\n")
while True:
    print("Please select an action from the following menu (type '5' to exit)")
    print("1 - Gather Data from a single sensor")
    print("2 - Calculate mean air quality in a given area")
    print("3 - Report all inactive sensors")
    choice = int(input())

    if choice == 1:
        id = input("Enter the id of the sensor:\n")
        start = input("Enter the start date of data collection (yyyy-mm-dd):\n")
        end = input("Enter the end date of collection (yyyy-mm-dd) or 'none' to collect a stamp\n")
        start = Date(start)
        if end != "none":
            end = Date(end)
        print(single_sensor(id, start, end))

    elif choice == 5:
        print("Thank you for choosing AQMS...")
        sys.exit()


# for sensor in sensors:
#   if in_range(sensor.get_loc()):
#      print(str(sensor))



