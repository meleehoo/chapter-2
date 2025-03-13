am = []
khong = []
duong = []
while True:
    inp = input("Nhập số nguyên (enter để dừng): ")
    if inp == "":
        break
    num = int(inp)
    if num < 0:
        am.append(num)
    elif num == 0:
        khong.append(num)
    else:
        duong.append(num)
for num in am + khong + duong:
    print(num)