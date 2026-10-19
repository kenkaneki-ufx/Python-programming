t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    nums = list(map(int, input().split()))[:n]
    if x in nums:
        first = nums.index(x) + 1
        last = n - nums[::-1].index(x)
        print(first, last)
    else:
        print(-1, -1)
