T_a = float(input("Nhập nhiệt độ không khí (°C): "))
V = float(input("Nhập tốc độ gió (km/h): "))
WCI = 13.12 + 0.6215 * T_a - 11.37 * (V ** 0.16) + 0.3965 * T_a * (V ** 0.16)
print("Chỉ số gió lạnh:", round(WCI))