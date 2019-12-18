import csv, sys
from sensor import Sensor
from date import Date
from option1 import single_sensor
from option2 import location_mean
from option3 import status
from option4 import similar_values

# List of sensors, their reading counts, and aqi descriptions
sensors = []
statuses = {}
reports = ["Extremely Bad", "Very Bad", "Bad", "Poor", "Rather Poor", "Insufficient", "Moderate", "Acceptable",
           "Quite Good", "Good", "Excellent"]


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
    print("4 - Group similar sensor readings over a given time")
    choice = int(input())

    if choice == 1:
        id = input("Enter the id of the sensor (Sensor#):\n")
        start = input("Enter the start date of data collection (yyyy-mm-dd):\n")
        end = input("Enter the end date of collection (yyyy-mm-dd) or 'none' to collect a stamp\n")
        start = Date(start)
        if end == "none":
            result = "Aggregation of " + id + " on " + str(start) + ": "
            answer = single_sensor(id, start)
            if isinstance(answer, int):
                result += str(answer) + " - " + reports[answer]
            else:
                result += answer
            print("\n-------------------------------------------------------------")
            print(result)
            print("-------------------------------------------------------------\n")
        else:
            end = Date(end)
            result = "Aggregation of " + id + " from " + str(start) + " to " + str(end) + ": "
            answer = single_sensor(id, start, end)
            if isinstance(answer, int):
                result += str(answer) + " - " + reports[answer]
            else:
                result += answer
            print("\n-------------------------------------------------------------")
            print(result)
            print("-------------------------------------------------------------\n")

    elif choice == 2:
        shape = input("Are you surveying a circle or square area? (square/circle)\n")
        min_lat = min_long = max_lat = max_long = radius = "none"
        if shape == "square":
            print("Enter the minimum latitude followed by the maximum latitude:")
            min_lat = float(input())
            max_lat = float(input())
            print("Enter the minimum longitude followed by the maximum longitude:")
            min_long = float(input())
            max_long = float(input())
        else:
            print("Enter the latitude and longitude of your circles center:")
            min_lat = float(input())
            min_long = float(input())
            radius = float(input("Enter the radius of your circular area:\n"))

        start = input("Enter the start date of data collection (yyyy-mm-dd):\n")
        end = input("Enter the end date of collection (yyyy-mm-dd) or 'none' to collect a stamp\n")
        start = Date(start)
        print("Processing....\n")
        if end == "none":
            if start.get_year() == "none":
                print("Invalid date format")
            else:
                result = "Aggregation of sensors in given area on " + str(start) + ": "
                answer = location_mean(sensors, start, "none", min_lat, min_long, radius, max_lat, max_long)
                if isinstance(answer, int):
                    result += str(answer) + " - " + reports[answer]
                else:
                    result += answer
                print("\n-------------------------------------------------------------")
                print(result)
                print("-------------------------------------------------------------\n")
        else:
            end = Date(end)
            if start.get_year() == "none" or end.get_year() == "none":
                print("Invalid date format")
            else:
                result = "Aggregation of sensors in given area from " + str(start) + " to " + str(end) + ": "
                answer = location_mean(sensors, start, end, min_lat, min_long, radius, max_lat, max_long)
                if isinstance(answer,int):
                    result += str(answer) + " - " + reports[answer]
                else:
                    result += answer
                print("\n-------------------------------------------------------------")
                print(result)
                print("-------------------------------------------------------------\n")

    elif choice == 3:
        date = Date(input("Enter the date to view Sensors statuses (yyyy-mm-dd):\n"))
        if date.get_year() == "none":
            print("Incorrect date format \n")
        else:
            print("Processing...")
            print(status(sensors, statuses, str(date)))
    elif choice == 4:
        start = input("Enter the start date to compare sensor readings (yyyy-mm-dd):\n")
        end = input("Enter the end date of comparison (yyyy-mm-dd) or 'none' to compare one day\n")
        start = Date(start)
        print("Processing....")
        answer = ''
        if end == "none":
            answer = similar_values(sensors, start, "none")
            print(answer)
            print("-------------------------------------------------------------------------")
            print("Similarity in material readings on " + str(start) + ":\n")
        else:
            end = Date(end)
            answer = similar_values(sensors, start, end)
            print(answer)
            print("-------------------------------------------------------------------------")
            print("Similarity in material readings from " + str(start) + " to " + str(end) + ":\n")

        if answer == "There were no results":
            print(answer)
        else:
            print("O3 Values")
            print("--------------------------")
            for i in range(len(answer[0])):
                print("Cluster " + str(i+1) + ": " + str(answer[0][i]))
            print("\nNO2 Values")
            print("--------------------------")
            for i in range(len(answer[1])):
                print("Cluster " + str(i+1) + ": " + str(answer[1][i]))
            print("\nSO2 Values")
            print("--------------------------")
            for i in range(len(answer[2])):
                print("Cluster " + str(i+1) + ": " + str(answer[2][i]))
            print("\nPM10 Values")
            print("--------------------------")
            for i in range(len(answer[3])):
                print("Cluster " + str(i+1) + ": " + str(answer[3][i]))
        print("\n----------------------------------------------------------------------------\n")

    elif choice == 5:
        print("Thank you for choosing AQMS...")
        sys.exit()




