def season_events():
    try:
        number_of_month = int(input("Введите номер месяца вашего рождения (1-12): "))

        if number_of_month < 1 or number_of_month > 12:
            print("Ошибка: номер месяца должен быть от 1 до 12.")
            return

        if number_of_month in [12, 1, 2]:
            season = "зима"
            events = "За окном падал белый снег"
        elif number_of_month in [3, 4, 5]:
            season = "весна"
            events = "Птицы пели прекрасные песни"
        elif number_of_month in [6, 7, 8]:
            season = "лето"
            events = "Солнце светило ярче чем когда-либо"
        else:
            season = "осень"
            events = "Урожай был невероятным"

        months = [
            "январь", "февраль", "март", "апрель", "май", "июнь",
            "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"
        ]
        month_name = months[number_of_month - 1]

        print(f"Вы родились в {month_name}. {events}.")

    except ValueError:
        print("Ошибка: введите целое число от 1 до 12.")


season_events()