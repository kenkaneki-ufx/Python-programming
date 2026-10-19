t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))[:n]
    counts = {}
    for value in nums:
        counts[value] = counts.get(value, 0) + 1
    best_value = -1
    best_count = -1
    for value in range(1, 101):
        count = counts.get(value, 0)
        if count > best_count:
            best_value = value
            best_count = count
    print(best_value, best_count)
