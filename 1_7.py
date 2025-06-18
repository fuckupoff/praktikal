def http(lst):
    return [s for s in lst if s.startswith("http://")]

strings = ["http://пример", "https://пример", "http://сайт", "hhhtp://привет", "привет"]
print(http(strings))