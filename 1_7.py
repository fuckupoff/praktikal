strs = [
        "http://youtube.com",
        "https://www.youtube.com",
        "http://google.com",
        "ftp://files.com",
        "http://yandex.ru",
        "null",
        "https://github.com"
]
res = []
for i in strs:
        if i.startswith("http://"):
                res.append(i)
print(res)
