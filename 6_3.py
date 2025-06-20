from datetime import datetime

class Task:
    def __init__(self, date_start: str, date_finish: str, description: str):
        self.date_start = datetime.strptime(date_start, "%d.%m.%Y %H:%M")
        self.date_finish = datetime.strptime(date_finish, "%d.%m.%Y %H:%M")
        self.description = description

tasks = [
    Task("01.09.2023 10:00", "01.09.2023 12:00", "Лекция по Python"),
    Task("02.09.2023 14:00", "02.09.2023 18:00", "Практика по SQL"),
    Task("03.09.2023 09:00", "03.09.2023 11:00", "Семинар по алгоритмам"),
    Task("04.09.2023 13:00", "04.09.2023 20:00", "Марафон кодинга"),
    Task("05.09.2023 10:00", "05.09.2023 15:00", "Разбор домашних заданий")
]

latest_task = max(tasks, key=lambda task: task.date_finish)

print(f"Позже всех заканчивается: {latest_task.description}")