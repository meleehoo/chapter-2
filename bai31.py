def caesar_cipher(text, shift=3):
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
encoded = caesar_cipher(message)
print("Tin nhắn mã hóa:", encoded)