n = int(input())
word = [input() for _ in range(n)]

# Write your code here!
word.sort()

for i in word:
    print(i)