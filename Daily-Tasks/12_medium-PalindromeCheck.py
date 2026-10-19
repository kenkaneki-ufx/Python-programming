t = int(input())
for _ in range(t):
    word = input().strip()
    mismatches = sum(1 for i in range(len(word) // 2) if word[i] != word[-1 - i])
    print("YES 0" if mismatches == 0 else f"NO {mismatches}")
