C = 4.186  # J/g°C
M = float(input("Nhập khối lượng nước (gram): "))
delta_T = float(input("Nhập thay đổi nhiệt độ (°C): "))
Q = M * C * delta_T
energy_kWh = Q * 2.777e-7
cost = energy_kWh * 8.9
print("Năng lượng cần thiết:", Q, "Joules")
print("Chi phí:", cost, "cents")