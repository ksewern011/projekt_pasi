class Client:
    def __init__(self, name):
        self.name = name

    def order_transport(self, service):
        print(f"\n{self.name} złożył zamówienie")
        service.order_transport()

