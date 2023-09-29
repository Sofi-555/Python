from Hotel import Hotel
from HotelRoom import HotelRoom
from HotelCustomer import HotelCustomer
from hotel_types import Service,ResortHotel, BoutiqueHotel, BusinessHotel


def main():
    hotels = []

    hotel1 = Hotel("Готель 1")
    hotel2 = Hotel("Готель 2")
    hotel3 = ResortHotel("Resort Hotel")
    hotel4 = BoutiqueHotel("Boutique Hotel")
    hotel5 = BusinessHotel("Business Hotel")

    hotels.append(hotel1)
    hotels.append(hotel2)
    hotels.append(hotel3)
    hotels.append(hotel4)
    hotels.append(hotel5)

    room1 = HotelRoom(101, 100)
    room2 = HotelRoom(102, 150)
    room3 = HotelRoom(103, 200)
    room4 = HotelRoom(201, 120)
    room5 = HotelRoom(202, 180)

    hotel1.add_room(room1)
    hotel1.add_room(room2)
    hotel1.add_room(room3)
    hotel1.add_room(room4)
    hotel1.add_room(room5)


    while True:
        print("\nОберіть опцію:")
        print("1. Вибрати готель")
        print("2. Подивитися вільні номери")
        print("3. Забронювати кімнату")
        print("4. Додати відгук")
        print("5. Викликати сервіс")
        print("6. Відгуки про готель")
        print("7. Спеціальний івент")
        print("8. Вийти з програми")

        choice = input("Введіть номер опції: ")

        if choice == '1':
            print("Список доступних готелів:")
            for i, hotel in enumerate(hotels):
                print(f"{i + 1}. {hotel.name}")
            hotel_choice = int(input("Виберіть номер готелю: ")) - 1

            if 0 <= hotel_choice < len(hotels):
                current_hotel = hotels[hotel_choice]
                print(f"Ви вибрали готель: {current_hotel.name}")
            else:
                print("Невірний вибір готелю.")

        elif choice == '2':
            if 'current_hotel' in locals():
                free_rooms = current_hotel.get_free_rooms()
                if free_rooms:
                    print(f"Вільні номери в готелі '{current_hotel.name}':")
                    for room in free_rooms:
                        print(room)
                else:
                    print(f"У готелі '{current_hotel.name}' немає вільних номерів.")
            else:
                print("Спершу виберіть готель.")

        elif choice == '3':
            if 'current_hotel' in locals():
                room_number = int(input("Введіть номер кімнати, яку ви бажаєте забронювати: "))
                first_name = input("Введіть ваше ім'я: ")
                last_name = input("Введіть ваше прізвище: ")
                check_in_date = input("Введіть дату заселення: ")
                check_out_date = input("Введіть дату виселення: ")

                customer = HotelCustomer(first_name, last_name)
                result = current_hotel.book_room(room_number, customer, check_in_date, check_out_date)
                print(result)
            else:
                print("Спершу виберіть готель.")

        elif choice == '4':
            if 'current_hotel' in locals():
                first_name = input("Введіть ваше ім'я: ")
                last_name = input("Введіть ваше прізвище: ")
                review = input("Введіть ваш відгук: ")
                rating = input("Введіть рейтинг (від 1 до 5): ")

                customer = HotelCustomer(first_name, last_name)
                result = current_hotel.add_review(customer, review, rating)
                print(result)
            else:
                print("Спершу виберіть готель.")

        elif choice == '5':
            if 'current_hotel' in locals():
                room_number = int(input("Введіть номер кімнати, для якої викликаєте рум-сервіс: "))
                current_hotel.call_service(room_number)
            else:
                print("Спершу виберіть готель.")

        elif choice == '6':
            if 'current_hotel' in locals():
                reviews = current_hotel.reviews
                if reviews:
                    print("Всі відгуки:")
                    for review in reviews:
                        print(f"Клієнт: {review['Клієнт']} Рейтинг: {review['Рейтинг']} Відгук: {review['Відгук']}")
                else:
                    print("У цьому готелі ще немає відгуків.")
            else:
                print("Спершу виберіть готель.")

        elif choice == '7':
            if 'current_hotel' in locals():
                event_description = current_hotel.special_event()
                print(event_description)
            else:
                print("Спершу виберіть готель.")

        elif choice == '8':
            break

        else:
            print("Невідома опція. Будь ласка, введіть правильний номер опції.")

if __name__ == '__main__':
    main()