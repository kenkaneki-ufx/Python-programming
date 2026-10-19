t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))[:n]
    is_sorted = all(nums[i] >= nums[i - 1] for i in range(1, n))
    print("YES" if is_sorted else "NO")
