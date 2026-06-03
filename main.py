from clients import *
from services import *

def main():

    client1 = Client("Jan Kowalski")
    client2 = Client("Włodzimierz Biały")
    bike_service = BikeService()



    client1.order_transport(bike_service)
    client2.order_transport(bike_service)

if True:
    main()



