from collections import defaultdict

class FitnessCenter:
    def __init__(self, client_code: str, year: int, month: int, duration: int):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

sessions = [
    FitnessCenter("A001", 2023, 1, 60),
    FitnessCenter("A002", 2023, 2, 45),
    FitnessCenter("A003", 2022, 3, 90),
    FitnessCenter("A004", 2022, 4, 30),
    FitnessCenter("A005", 2023, 5, 120),
    FitnessCenter("A006", 2022, 6, 180),
    FitnessCenter("A007", 2023, 7, 60),
    FitnessCenter("A008", 2021, 8, 45),
    FitnessCenter("A009", 2021, 9, 90),
    FitnessCenter("A010", 2023, 10, 150)
]

yearly_duration = defaultdict(int)
for session in sessions:
    yearly_duration[session.year] += session.duration

max_year = min(
    [year for year, duration in yearly_duration.items() if duration == max(yearly_duration.values())]
)

print(f"Год с наибольшей продолжительностью: {max_year} ({yearly_duration[max_year]} мин)")