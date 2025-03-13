ds = []
while True:
    word = input("Nhập từ (enter để dừng): ")
    if word == "":
        break
    if word not in ds:
        ds.append(word)
for word in ds:
    print(word)