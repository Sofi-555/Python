from Hotel import Hotel

class Service:
    def __init__(self):
        self.services = []
    
    def add_service(self,service_name):
        self.services.append(service_name)
    
class BoutiqueHotel(Hotel,Service):
    def __init__(self):
        super().__init__()
        self.services.append("Замовити їжу")
        self.services.append("Замовити приватний трансфер")
        self.services.append("Технічні послуги")
        
class BusinessHotel(Hotel,Service):
    def __init__(self):
        super().__init__()
        self.services.append("Замовити конференс зал 1 класу")
        self.services.append("Замовити конференс зал 2 класу")

class ResortHotel(Hotel,Service):
    def __init__(self):
        super().__init__()
        self.services.append("Замовити спа")
        self.services.append("Замовити спортивний зал")
        self.services.append("Замовити басейн")

