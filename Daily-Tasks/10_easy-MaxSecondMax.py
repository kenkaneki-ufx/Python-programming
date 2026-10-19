t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))[:n]
    unique = sorted(set(nums), reverse=True)
    print(unique[0], unique[1])
