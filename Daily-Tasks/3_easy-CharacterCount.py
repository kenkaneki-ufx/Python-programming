t = int(input())
for _ in range(t):
    word = input().strip()
    vowels = sum(1 for ch in word if ch in "aeiou")
    print(vowels, len(word) - vowels)
