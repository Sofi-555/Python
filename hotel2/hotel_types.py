from Hotel import Hotel

class BoutiqueHotel(Hotel):
    def special_event(self):
        return "Ексклюзивний рум сервіс викликано."

class BusinessHotel(Hotel):
    def special_event(self):
        return "У готелі пройшла бізнес зустріч акціонерів Apple."

class ResortHotel(Hotel):
    def special_event(self):
        return "У готелі відбувся музичний фестиваль."
