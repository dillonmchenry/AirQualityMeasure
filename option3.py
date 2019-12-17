from date import Date


# edits idiotic csv file
def fixline(line):
    new = []
    for i in range(1, len(line), 2):
        new.append(line[i])
    final = "".join(new)
    return final.split(";")


# Option 3
def status(sensors, statuses, stamp):
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

