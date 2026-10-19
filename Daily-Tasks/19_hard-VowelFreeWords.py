t = int(input())
for _ in range(t):
    m = int(input())
    words = input().split()[:m]
    vowel_free = sum(1 for word in words if all(ch not in "aeiou" for ch in word))
    print(vowel_free)
