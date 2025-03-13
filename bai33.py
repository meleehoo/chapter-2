def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

chuoi = input("Nhập chuỗi: ")
if is_palindrome(chuoi):
    print("Đây là palindrome")
else:
    print("Đây không là palindrome")