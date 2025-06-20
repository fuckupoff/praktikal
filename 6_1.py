names = ["Алексей", "Мария", "Анна", "Иван", "Арина", "Дмитрий", "Алиса", "Сергей", "Андрей", "Ольга"]

names_with_a = []
for i in names:
    if i.startswith(('А', 'A')):
        names_with_a.append(i)
print(names_with_a)