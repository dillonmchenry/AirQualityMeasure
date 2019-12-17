import math
from option1 import single_sensor


def in_square(loc, min, max):
    if min[0] <= loc[0] <= max[0] and min[1] <= loc[1] <= max[1]:
        return True
    else:
        return False


def in_circle(loc, center, radius):
    distance = math.sqrt((loc[0]-float(center[0]))**2 + (loc[1]-float(center[1]))**2)
    if distance < radius:
        return True
    return False


def location_mean(sensors, start, end, lat_min, long_min, radius="none", lat_max="none", long_max="none"):
    # Finds sensors in bounds of border
    in_bounds = []
    if radius != "none":
        for sensor in sensors:
            if in_circle(sensor.get_loc(), [lat_min, long_min], radius):
                in_bounds.append(sensor)
    else:
        for sensor in sensors:
            if in_square(sensor.get_loc(), [lat_min, lat_max], [lat_max, long_max]):
                in_bounds.append(sensor)

    # Averages sensor reading averages
    average = 0
    for sensor in in_bounds:
        average += single_sensor(sensor.get_id(), start, end)
    if len(in_bounds) > 0:
        return math.floor(average/len(in_bounds))
    else:
        return "There were no results..."

