import csv,sys, math
from sensor import Sensor
from date import Date
# List of sensors
sensors = []


# Option 1
def single_sensor(id, start, end="none"):
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


# Option 2
def location_mean(start, end, lat_min, long_min, radius="none", lat_max="none", long_max="none"):
    in_bounds = []
    if radius:
        for sensor in sensors:
            if in_circle(sensor.get_loc(), [lat_min, long_min], radius):
                in_bounds.append(sensor)
    else:
        for sensor in sensors:
            if in_square(sensor.get_loc(), [lat_min, lat_max], [lat_max, long_max]):
                in_bounds.append(sensor)

    for sensor in in_bounds:
        # Call single sensor over the timespan for each sensor
        single_sensor(sensor.get_id(), start, end)


def fixline(line):
    new = []
    for i in range(1, len(line), 2):
        new.append(line[i])
    final = "".join(new)
    return final.split(";")


# Tests if lat long is in range of given parameters
def in_square(loc, min, max):
    if min[0] <= loc[0] <= max[0] and min[1] <= loc[1] <= max[1]:
        return True
    else:
        return False


def in_circle(loc, center, radius):
    distance = math.sqrt((loc[0]-center[0])**2 + (loc[1]-center[1])**2)
    if distance < radius:
        return True
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
        if end == "none":
            print(single_sensor(id, start))
        print(single_sensor(id, start, end))

    elif choice == 2:
        print("YO")
        # Implement User interaction here

    elif choice == 5:
        print("Thank you for choosing AQMS...")
        sys.exit()


# for sensor in sensors:
#   if in_range(sensor.get_loc()):
#      print(str(sensor))



