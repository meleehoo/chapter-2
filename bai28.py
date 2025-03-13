month = input("Nhập tên tháng: ").lower()
if month in ["january", "march", "may", "july", "august", "october", "december"]:
    print("31 ngày")
elif month in ["april", "june", "september", "november"]:
    print("30 ngày")
elif month == "february":
    print("28 hoặc 29 ngày")
else:
    print("Tên tháng không hợp lệ")