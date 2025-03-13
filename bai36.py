ds = []
while True:
    num = int(input("Nhập số nguyên (0 để dừng): "))
    if num == 0:
        break
    ds.append(num)
ds.sort()
for num in ds:
    print(num)