class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive_method(self):
        return "Vroom vroom"