import pytest
from services import *
from transport import *

def test_tworzenie_transportu():
    service = BikeService()
    pojazd = service.create_transport()
    assert isinstance(pojazd, Bike)
def test_dzialanie_metod():
    service = BikeService()
    pojazd = service.create_transport()
    assert pojazd.vehicle_type() == "Bike"
    assert pojazd.arrival_time() == "5 minutes"
def test_mechanizm_dostepnosci():
    service = BikeService()
    service.order_transport()
    assert service.available == False




