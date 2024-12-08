import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.area = self.calculate_area()

    def calculate_area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def __repr__(self):
        return f"{self.a} {self.b} {self.c}"



n = int(input())
triangles = []

for i in range(n):
    a, b, c = map(int, input().split())
    triangles.append(Triangle(a, b, c))


triangles.sort(key=lambda triangle: triangle.area)


for triangle in triangles:
    print(triangle)
