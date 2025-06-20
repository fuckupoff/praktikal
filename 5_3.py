import random

def generate_even_array(length: int, max_num: int) -> list:
    return sorted(random.sample(range(0, max_num + 1, 2), k=length))

print(generate_even_array(5, 20))