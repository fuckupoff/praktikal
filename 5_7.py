import math

def is_point_in_circle(x: float, y: float, radius: float):
    distance = math.sqrt(x**2 + y**2)
    return distance <= radius

print(is_point_in_circle(3, 4, 5))
print(is_point_in_circle(6, 8, 5))