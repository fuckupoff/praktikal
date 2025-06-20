def get_user_division():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        result = a / b
        return f"Результат деления: {result:.2f}"

    except ValueError:
        return "Ошибка: введите числа"
    except ZeroDivisionError:
        return "Ошибка: деление на 0 невозможно"
    except Exception as e:
        return f"Неизвестная ошибка: {e}"

print(get_user_division())