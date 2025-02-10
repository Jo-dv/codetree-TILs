n = int(input())
words = [input() for _ in range(n)]

# Write your code here!
from collections import Counter
result = Counter(words)
answer = 0

for k, v in result.items():
    answer = max(answer, v)

print(answer)