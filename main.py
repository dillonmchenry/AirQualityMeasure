import csv, sys


lat_min = 0.0
lat_max = 70.0
long_min = -40.0
long_max = 100.0


def in_range(lat, long):
    if lat_min <= lat <= lat_max and long_min <= long <= long_max:
        return True
    else:
        return False


# Getting sensors in range
with open("sensors.csv", "rt") as f:
    entries = csv.DictReader(f, fieldnames=None, delimiter=';', quoting=csv.QUOTE_ALL)
    for row in entries:
        if in_range(float(row["Latitude"]), float(row["Longitude"])):
            print(row["SensorID"])


# Getting sensor info for aggregate?
with open("sensor_data.csv", "rt") as data:
    entries = csv.DictReader(f, fieldnames=None, delimiter=';', quoting=csv.QUOTE_ALL)
    print(next(entries))



