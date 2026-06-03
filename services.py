from transport import *
from abc import ABC, abstractmethod

class TransportService(ABC):
    def __init__(self):
        self.available = True

    @abstractmethod
    def create_transport(self):
        pass

    @abstractmethod
    def transport_name(self):
        pass

    def order_transport(self):
        if self.available:
            transport = self.create_transport()
            print(f"pomyślnie zamówiono: {self.transport_name()}")
            print(f"typ pojazdu: {transport.vehicle_type()}")
            print(f"przewidywany czas przyjazdu: {transport.arrival_time()}")
            print(f"przewidywany czas podróży: {transport.travel_time()}")
            self.available = False
        else:
            print(f"usługa {self.transport_name()} jest w tej chwili niedostępna")


class BikeService(TransportService):
    def create_transport(self):
        return Bike()

    def transport_name(self):
        return "Bike"
