a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a == b == c:
    print("Tam giác đều")
elif a == b or a == c or b == c:
    print("Tam giác cân")
else:
    print("Tam giác thường")