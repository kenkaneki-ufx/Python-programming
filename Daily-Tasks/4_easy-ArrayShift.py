t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))[:n]
    shifted = nums[-1:] + nums[:-1]
    print(*shifted)
