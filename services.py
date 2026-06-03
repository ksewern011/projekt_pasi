from transport import *
from abc import ABC, abstractmethod

class TransportService(ABC):

    @abstractmethod
    def create_transport(self):
        pass

    @abstractmethod
    def transport_name(self):
        pass

    def order_transport(self):
        transport = self.create_transport()
        print(f"pomyślnie zamówiono: {self.transport_name()}")
        print(f"typ pojazdu: {transport.vehicle_type()}")
        print(f"przewidywany czas przyjazdu: {transport.arrival_time()}")
        print(f"przewidywany czas podróży: {transport.travel_time()}")



class BikeService(TransportService):
    def create_transport(self):
        return Bike()

    def transport_name(self):
        return "Bike"

class TaxiService(TransportService):
    def create_transport(self):
        return Taxi()

    def transport_name(self):
        return "Taxi"

class ScooterService(TransportService):
    def create_transport(self):
        return Scooter()

    def transport_name(self):
        return "Scooter"

