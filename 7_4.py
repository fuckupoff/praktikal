class FitnessCenter:
    def __init__(self, client_code: str, year: int, month: int, duration: int):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

sessions = [
    FitnessCenter("A001", 2023, 1, 60),
    FitnessCenter("A002", 2023, 2, 45),
    FitnessCenter("A003", 2023, 3, 90),
    FitnessCenter("A004", 2023, 4, 30),
    FitnessCenter("A005", 2023, 5, 120)
]

longest_session = max(sessions, key=lambda x: x.duration)
shortest_session = min(sessions, key=lambda x: x.duration)

print(f"Самое долгое занятие: Код {longest_session.client_code}, {longest_session.duration} мин")
print(f"Самое короткое занятие: Код {shortest_session.client_code}, {shortest_session.duration} мин")