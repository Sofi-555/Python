import random

class Hotel:
    def __init__(self, hotel_name, services_available=set()):
        self.hotel_name = hotel_name
        self.services_available = services_available
  
class Service(Hotel):
    def __init__(self, service_name, services_available):
        super().__init__(service_name, services_available)
        self.service_name = service_name
  
    def provide_service(self, client):
        while any(client.needs.values()):
            for need, need_value in client.needs.items():
                if need in self.services_available and self.services_available[need] > 0:
                    if self.services_available[need] >= need_value:
                        client.needs[need] = 0
                    else:
                        client.needs[need] -= self.services_available[need]
            client.needs = {k: round(v, 2) for k, v in client.needs.items()}
            print(vars(client))

class BarService(Service):
    def __init__(self, service_name, services_available):
        super().__init__(service_name, services_available)
  
class Client:
    def __init__(self, client_name):
        self.client_name = client_name
        self.needs = self.generate_random_needs()

    def generate_random_needs(self):
        random_needs = {'eat', 'bar', 'child room', 'massage'}
        random_values = {need: round(random.uniform(0.1, 1.0), 1) for need in random.sample(random_needs, 2)}
    
        return random_values

client = Client("John")
hotel = Hotel("Business Hotel", services_available={"eat": 0.5, "bar": 0.35, "child room": 0.25, 'massage': 0.5})
service = Service(hotel.hotel_name, hotel.services_available)
service.provide_service(client)
