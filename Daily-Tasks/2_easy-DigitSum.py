t = int(input())
for _ in range(t):
    n = input().strip()
    digit_sum = sum(int(digit) for digit in n)
    print(digit_sum, "YES" if digit_sum % 3 == 0 else "NO")
