from datetime import datetime

def format_date(date_str: str):
    try:
        date_obj = datetime.strptime(date_str, "%d.%m.%Y")
        weekday = date_obj.strftime("%A")
        day = date_obj.day
        month = date_obj.strftime("%B")
        year = date_obj.year
        return f"{weekday}, {day} {month}, {year} год"
    except ValueError:
        return "Используйте ДД.ММ.ГГГГ"


input_date = (input("Введите дату: "))
print(format_date(input_date))