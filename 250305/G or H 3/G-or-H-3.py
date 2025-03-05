n, k = map(int, input().split())
x = []
c = []
temp = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(1 if char == "G" else 2)
    temp.append((int(pos), 1 if char == "G" else 2))

# Please write your code here.
temp.sort(key=lambda x: x[0])
answer = 0
low = 0
for high in range(len(temp)):
    if temp[high][0] - temp[low][0] <= k:
        score = 0
        for i in range(low, high + 1):
            score += temp[i][1]
    else:
        low += 1

    answer = max(answer, score)

print(answer)
