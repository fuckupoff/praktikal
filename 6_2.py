class User:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

users = [
    User("admin", "12345"),
    User("ivan", "qwerty"),
    User("alex", "password"),
    User("anna", "11111"),
    User("max", "zxcvbn")
]

def find_user(login: str, password: str):
    for user in users:
        if user.login == login and user.password == password:
            return user
    return None

found_user = find_user("ivan", "qwerty")
if found_user:
    print(f"Найден пользователь: {found_user.login}")
else:
    print("Пользователь не найден.")