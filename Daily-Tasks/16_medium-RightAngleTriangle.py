t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a * a + b * b == c * c or b * b + c * c == a * a or c * c + a * a == b * b:
        print("YES")
    else:
        print("NO")
