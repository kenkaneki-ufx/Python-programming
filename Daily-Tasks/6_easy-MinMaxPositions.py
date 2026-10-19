t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))[:n]
    min_position = nums.index(min(nums)) + 1
    max_position = nums.index(max(nums)) + 1
    print(min_position, max_position)
