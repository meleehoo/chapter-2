def print_longer(s1, s2):
    if len(s1) > len(s2):
        print(s1)
    elif len(s2) > len(s1):
        print(s2)
    else:
        print(s1)
        print(s2)

s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
print_longer(s1, s2)