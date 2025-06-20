numbers = [3, -5, -2, 8, 0, -1, 4]

first_positive = next(x for x in numbers if x > 0)
last_negative = next(x for x in reversed(numbers) if x < 0)

print(f"Первый положительный: {first_positive}")
print(f"Последний отрицательный: {last_negative}")