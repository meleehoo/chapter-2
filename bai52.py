def is_perfect(n):
    if n <= 1:
        return False
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_divisors == n

print("Các số hoàn hảo từ 1 đến 10,000:")
for num in range(1, 10001):
    if is_perfect(num):
        print(num)