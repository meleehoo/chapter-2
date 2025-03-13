def giaithua(n):
    if n == 0:
        return 1
    return n * giaithua(n - 1)

x = int(input("Nhập số cần tính giai thừa: "))
print("Giai thừa của", x, "là:", giaithua(x))