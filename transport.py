from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def vehicle_type(self):
        pass

    @abstractmethod
    def arrival_time(self):
        pass

    @abstractmethod
    def travel_time(self):
        pass


class Bike(Transport):

    def vehicle_type(self):
        return "Bike"

    def arrival_time(self):
        return "5 minutes"

    def travel_time(self):
        return "15 minutes"

class Taxi(Transport):

    def vehicle_type(self):
        return "Taxi"

    def arrival_time(self):
        return "4 minutes"

    def travel_time(self):
        return "5 minutes"

class Scooter(Transport):

    def vehicle_type(self):
        return "Scooter"

    def arrival_time(self):
        return "10 minutes"

    def travel_time(self):
        return "10 minutes"
