import math

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
C = float(input("Nhập góc C (radian): "))
S = 0.5 * a * b * math.sin(C)
print("Diện tích tam giác là:", S)