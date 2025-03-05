n, k = map(int, input().split())
temp = []
for _ in range(n):
    pos, char = input().split()
    temp.append((int(pos), 1 if char == "G" else 2))

# Please write your code here.
temp.sort(key=lambda x: x[0])
answer = 0
low = 0
score = 0

for high in range(len(temp)):
    score += temp[high][1]
    while temp[high][0] - temp[low][0] > k:
        score -= temp[low][1]
        low += 1

    answer = max(answer, score)

print(answer)
