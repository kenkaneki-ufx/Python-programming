t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))[:n]
    print(sum(nums) - min(nums))
