meal_cost = float(input("Nhập chi phí bữa ăn: "))
tax = 0.05 * meal_cost
tip = 0.18 * meal_cost
total_cost = meal_cost + tax + tip
print(f"Chi phí bữa ăn: {meal_cost:.2f}")
print(f"Thuế: {tax:.2f}")
print(f"Tiền boa: {tip:.2f}")
print(f"Tổng tiền: {total_cost:.2f}")