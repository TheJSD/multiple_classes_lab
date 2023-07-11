class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Vroom vroom"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def empty_bus(self):
        self.passengers.clear()
        # alternatively could do:
        # self.passengers = [] # resets to an empty list

    def pick_up_from_stop(self, bus_stop_to_pickup):
        for passenger in bus_stop_to_pickup.queue:
            self.passengers.append(passenger)
        bus_stop_to_pickup.clear()