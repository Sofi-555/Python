class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.booked_rooms = []
        self.reviews = []

    def get_free_rooms(self):
        free_rooms = []
        for room in self.rooms:
            if room.status == "Free":
                free_rooms.append(room)
            else:
                continue
        
        return free_rooms


    def add_room(self, room):
        self.rooms.append(room)

    def book_room(self, room_number, customer, check_in_date, check_out_date):
        for room in self.rooms:
            if room.status == "Free":
                room.status = "Booked"
                self.booked_rooms.append({"Кімната": room, "Клієнт": customer,"Дата заселення": check_in_date, "Дата виселення": check_out_date})
                return f"{customer} забронював номер {room_number} з {check_in_date} по {check_out_date}."
            else:
                return f"Room {room_number} is already booked."
        return f"Room {room_number} is not found."
    
    def add_review(self, customer, review, rating):
        self.reviews.append({"Клієнт": customer, "Рейтинг": rating, "Відгук": review})
        return f"{customer} залишив відгук про готель: \n Рейтинг: {rating} \n Відгук: {review}"
    
    def call_service(self, number):
        for room in self.booked_rooms:
            if room["Кімната"].number == number:
                print(f"У номер {number} викликано рум сервіс.")
                return
        print(f"У номері {number} рум сервіс не викликано.")

    def special_event(self):
        return "Це звичайний готель і тут немає особливих івентів."
            








        