t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))[:n]
    even_count = sum(1 for x in nums if x % 2 == 0)
    print(even_count, n - even_count)
