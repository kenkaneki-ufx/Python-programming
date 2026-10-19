t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))[:n]
    print(sum(1 for x in nums if x % k == 0))
