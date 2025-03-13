def format_list(words):
    if len(words) == 0:
        return ""
    elif len(words) == 1:
        return words[0]
    else:
        return ", ".join(words[:-1]) + " and " + words[-1]

words = input("Nhập các từ, cách nhau bởi dấu cách: ").split()
print(format_list(words))