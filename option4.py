from date import Date


def fixline(line):
    new = []
    for i in range(1, len(line), 2):
        new.append(line[i])
    final = "".join(new)
    # Slice to remove double quote in front
    return final[1:].split(";")


def sort_measures(grouped_list, data, sensor, material, threshold):
    added = False
    for i in range(len(grouped_list)):
        if abs(data[sensor.get_id()][material] - data[grouped_list[i][0]][material]) <= threshold and not added:
            grouped_list[i].append(sensor.get_id())
            added = True
    if not added:
        grouped_list.append([sensor.get_id()])

    return grouped_list


def similar_values(sensors, start, end):
    readings = {}
    for sensor in sensors:
        readings[sensor.get_id()] = {"O3": 0, "NO2": 0, "SO2": 0, "PM10": 0}

    count = 0
    with open("data_10sensors_1year.csv", "rt") as data:
        reader = data.readlines()

        for i in range(2, len(reader)-1, 2):
            real = fixline(reader[i])
            # checks id
            curr = Date(real[0].split("T")[0])
            # checks time span
            if curr.in_span(start, end):
                readings[real[1]][real[2]] += float(real[3])
                count += 1
            real.clear()
        if count == 0:
            print("There were no results")
        else:
            o3, no2, so2, pm10 = [[]], [[]], [[]], [[]]
            for sensor in sensors:
                # first sensor
                if len(o3[0]) == 0:
                    o3[0].append(sensor.get_id())
                    no2[0].append(sensor.get_id())
                    so2[0].append(sensor.get_id())
                    pm10[0].append(sensor.get_id())
                else:
                    o3 = sort_measures(o3, readings, sensor, "O3", count/7.5)
                    no2 = sort_measures(no2, readings, sensor, "NO2", count/7.5)
                    so2 = sort_measures(so2, readings, sensor, "SO2", count/7.5)
                    pm10 = sort_measures(pm10, readings, sensor, "PM10", count/(7.5*5))
        print(count)
        return [o3, no2, so2, pm10]





