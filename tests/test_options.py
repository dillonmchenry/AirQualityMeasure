from option1 import single_sensor
from date import Date

d1 = Date("2017-04-03")

def test_single_sensor():
    assert True
    assert single_sensor("Sensor0", d1) == 9
    assert single_sensor("Sensor4", d1, Date("2017-04-09")) == 9
    assert single_sensor("Sensor5", Date("2018-07-04")) == "There were no results..."

def test_location_mean():
    assert True

def test_status():
    assert True