import csv
from date import Date
from sensor import Sensor
from option1 import single_sensor
from option2 import location_mean
from option3 import status
from option4 import similar_values

sensors = []
statuses = {}

# Collects all sensors in list and initializes status dictionary
with open("sensors.csv", "rt") as f:
    entries = csv.DictReader(f, fieldnames=None, delimiter=";", quoting=csv.QUOTE_ALL)
    for row in entries:
        sensors.append(Sensor(row["SensorID"], float(row["Latitude"]), float(row["Longitude"])))
    for sensor in sensors:
        statuses[sensor.get_id()] = [0, 0]  # hits and negative hits
    

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
    assert status(sensors, statuses, Date("2017-10-09")) == """Sensor0: 192 hits, 0 negative readings 
Sensor1: 192 hits, 0 negative readings 
Sensor2: 192 hits, 0 negative readings 
Sensor3: 192 hits, 0 negative readings 
Sensor4: 192 hits, 0 negative readings 
Sensor5: 192 hits, 0 negative readings 
Sensor6: 192 hits, 0 negative readings 
Sensor7: 192 hits, 0 negative readings 
Sensor8: 192 hits, 0 negative readings 
Sensor9: 192 hits, 0 negative readings 
"""

def test_similar_values():
    assert similar_values(sensors, Date("2017-03-11"), Date("2017-03-12")) == [
        [['Sensor0', 'Sensor3', 'Sensor4', 'Sensor8', 'Sensor9'], 
        ['Sensor1', 'Sensor2', 'Sensor5', 'Sensor6', 'Sensor7']], 
        [['Sensor0', 'Sensor8'], 
        ['Sensor1', 'Sensor2', 'Sensor4', 'Sensor5', 'Sensor7', 'Sensor9'], 
        ['Sensor3', 'Sensor6']], 
        [['Sensor0', 'Sensor2', 'Sensor3', 'Sensor7', 'Sensor9'], 
        ['Sensor1', 'Sensor4', 'Sensor5', 'Sensor6', 'Sensor8']], 
        [['Sensor0', 'Sensor2', 'Sensor3', 'Sensor4', 'Sensor6', 'Sensor7', 'Sensor8', 'Sensor9'], 
        ['Sensor1', 'Sensor5']]]

    assert similar_values(sensors, Date("2017-06-21"), "none") == [
        [['Sensor0', 'Sensor2'],
         ['Sensor1', 'Sensor5', 'Sensor6', 'Sensor8'],
         ['Sensor3', 'Sensor7'],
         ['Sensor4'], ['Sensor9']],
         [['Sensor0', 'Sensor1', 'Sensor5'],
         ['Sensor2', 'Sensor7', 'Sensor9'],
         ['Sensor3', 'Sensor8'],
         ['Sensor4', 'Sensor6']],
         [['Sensor0', 'Sensor1'],
         ['Sensor2', 'Sensor4', 'Sensor5'], 
         ['Sensor3'], ['Sensor6', 'Sensor7'],
         ['Sensor8'], ['Sensor9']], [['Sensor0', 'Sensor9'],
         ['Sensor1', 'Sensor2'], 
         ['Sensor3', 'Sensor5', 'Sensor8'], ['Sensor4', 'Sensor7'], ['Sensor6']]]