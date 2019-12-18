import csv
from date import Date
from sensor import Sensor
from option1 import single_sensor
from option2 import location_mean

sensors = []

# Collects all sensors in list and initializes status dictionary
with open("sensors.csv", "rt") as f:
    entries = csv.DictReader(f, fieldnames=None, delimiter=";", quoting=csv.QUOTE_ALL)
    for row in entries:
        sensors.append(Sensor(row["SensorID"], float(row["Latitude"]), float(row["Longitude"])))
    

def test_single_sensor():
    d1 = Date("2017-04-03")
    assert single_sensor("Sensor0", d1) == 9
    assert single_sensor("Sensor4", d1, Date("2017-04-09")) == 9
    assert single_sensor("Sensor5", Date("2018-07-04")) == "There were no results..."

def test_location_mean():
    assert location_mean(sensors, Date("2017-02-04"), Date("2017-03-01"), 33.0, 15.0, 20.0) == 9
    assert location_mean(sensors, Date("2017-10-10"), "none", 0.0, -10.0, "none", 50.0, 70.) == 9
    assert location_mean(sensors, Date("2018-04-06"), "none", 0.0, 0.0, 0.0, "none", "none") == "There were no results..."

def test_status():
    assert True