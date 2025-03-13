def is_good_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit

password = input("Nhập mật khẩu: ")
if is_good_password(password):
    print("Mật khẩu tốt")
else:
    print("Mật khẩu không tốt")