
events_list = [(1798, "Видання Енеїди І.Котляревського"),
               (1991, "Pік отримання Україною незалежності від Радянського Союзу"),
               (1986, "Pік Чорнобильської катастрофи"),
               (2014, "Рік початку Революції Гідності та подій на майдані які привели до політичних змін України")]

time_dict = dict(events_list)

years_to_visit = {1798, 1991, 1986, 2014}  

for year in years_to_visit:
    try:
        event = time_dict[year]
        print(f"У році {year} відбулася подія: {event}")
    except KeyError:
        print(f"У році {year} немає відомих подій в історії.")
