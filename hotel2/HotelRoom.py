class HotelRoom:
    def __init__(self, number, price, customer=None, status="Free"):
        self.number = number
        self.price = price
        self.customer = customer
        self.status = status

    def __str__(self):
        if self.status == "Free":
            return f"Вільний номер {self.number} \n Ціна за одну ніч: {self.price}"
        else:
            return f"Номер {self.number} \n У номері перебуває клієнт {self.customer} \n"