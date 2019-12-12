import csv,sys, math
from sensor import Sensor
from date import Date

# List of sensors
sensors = []
statuses = {}
# ---------------------------FUNCTIONS FOR USER OPTIONS------------------------------


# Option 1
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
                measures[key] /= count/4.0
            # Mobo's function call will be the return of the function
            return measures


# Option 2
def location_mean(start, end, lat_min, long_min, radius="none", lat_max="none", long_max="none"):
    # Finds sensors in bounds of border
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
        # Average the value of single sensor averages
        single_sensor(sensor.get_id(), start, end)


def status(stamp):
    with open("data_10sensors_1year.csv", "rt") as data:
        reader = data.readlines()
        # Breaks up stupid ass csv
        real = []
        for i in range(2, len(reader)-1, 2):
            real = fixline(reader[i])
            if str(Date(real[0].split("T")[0])) == str(stamp):
                if float(real[3]) >= 0.0:
                    statuses[real[1]][0] += 1
                else:
                    statuses[real[1]][1] += 1
        result = ""
        for sensor in sensors:                         # Gets number of hits
            result += sensor.get_id() + ": " + str(statuses[sensor.get_id()][0]) + ' hits, ' + str(statuses[sensor.get_id()][1]) + " negative readings \n"
        return result

# -----------------------------------------------------------------------------------------


# edits idiotic csv file
def fixline(line):
    new = []
    for i in range(1, len(line), 2):
        new.append(line[i])
    final = "".join(new)
    return final.split(";")

# ------------------------------ Checks if sensor is in area ----------------------------


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

# -----------------------------------Main Program Flow-------------------------------------


# Collects all sensors in list and initializes status dictionary
with open("sensors.csv", "rt") as f:
    entries = csv.DictReader(f, fieldnames=None, delimiter=";", quoting=csv.QUOTE_ALL)
    for row in entries:
        sensors.append(Sensor(row["SensorID"], float(row["Latitude"]), float(row["Longitude"])))
    for sensor in sensors:
        statuses[sensor.get_id()] = [0, 0]  # hits and negative hits


# Menu Flow
print("Welcome to The Air Quality Management System!\n")
while True:
    print("Please select an action from the following menu (type '5' to exit)")
    print("1 - Gather Data from a single sensor")
    print("2 - Calculate mean air quality in a given area")
    print("3 - Report all sensor statuses at given time")
    choice = int(input())

    if choice == 1:
        id = input("Enter the id of the sensor (Sensor#):\n")
        start = input("Enter the start date of data collection (yyyy-mm-dd):\n")
        end = input("Enter the end date of collection (yyyy-mm-dd) or 'none' to collect a stamp\n")
        start = Date(start)
        if end == "none":
            print(single_sensor(id, start))
        else:
            end = Date(end)
            print(single_sensor(id, start, end))

    elif choice == 2:
        shape = input("Are you surveying a circle or square area? (square/circle)\n")
        min_lat = min_long = max_lat = max_long = cent_lat = cent_long = radius = "none"
        if shape == "square":
            print("Enter the minimum latitude followed by the maximum latitude:\n")
            min_lat = float(input())
            max_lat = float(input())
            print("Enter the minimum longitude followed by the maximum longitude:\n")
            min_long = float(input())
            max_long = float(input())
        else:
            print("Enter the latitude and longitude of your circles center:")
            cent_lat = float(input())
            cent_long = float(input())
            radius = float(input("Enter the radius of your circular area:\n"))

        start = input("Enter the start date of data collection (yyyy-mm-dd):\n")
        end = input("Enter the end date of collection (yyyy-mm-dd) or 'none' to collect a stamp\n")

        # Option 2 function call
    elif choice == 3:
        date = input("Enter the date to view Sensors statuses (yyyy-mm-dd):\n")
        print(status(date))

    elif choice == 5:
        print("Thank you for choosing AQMS...")
        sys.exit()




