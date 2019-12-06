import csv

with open("sensors.csv", "rt") as f:
    entries = csv.DictReader(f, fieldnames=None, delimiter=';', quoting=csv.QUOTE_ALL)


