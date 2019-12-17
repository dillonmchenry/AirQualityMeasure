class Sensor:
    id = 0
    lat = 0
    long = 0

    def __init__(self, id, lat, long):
        self.id = id
        self.lat = lat
        self.long = long

    def get_loc(self):
        return self.lat, self.long

    def get_id(self):
        return self.id

    def __str__(self):
        return "ID: " + self.id + ", Lat: " + str(self.lat) + ", Long: " + str(self.long)
