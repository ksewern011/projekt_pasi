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


