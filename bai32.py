def caesar_cipher(text, shift, decode=False):
    if decode:
        shift = -shift
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

message = input("Nhập tin nhắn: ")
shift = int(input("Nhập số ký tự dịch chuyển: "))
encoded = caesar_cipher(message, shift)
decoded = caesar_cipher(encoded, shift, decode=True)
print("Tin nhắn mã hóa:", encoded)
print("Tin nhắn giải mã:", decoded)