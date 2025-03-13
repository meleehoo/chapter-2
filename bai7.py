num = int(input("Nhập một số: "))
level = int(input("Nhập bậc: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** level
    temp //= 10
if num == sum:
    print(num, "là số Armstrong bậc", level)
else:
    print(num, "không là số Armstrong")