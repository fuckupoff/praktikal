def modify_string(s: str):
    if s.startswith("abc"):
        return "www" + s[3:]
    else:
        return s + "zzz"

print(modify_string("abc123"))
print(modify_string("hello"))