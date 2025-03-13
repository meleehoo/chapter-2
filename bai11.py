length = float(input("Nhập chiều dài cánh đồng (mét): "))
width = float(input("Nhập chiều rộng cánh đồng (mét): "))
area_m2 = length * width
area_acres = area_m2 / 43.560
print("Diện tích cánh đồng là:", area_acres, "Acre")