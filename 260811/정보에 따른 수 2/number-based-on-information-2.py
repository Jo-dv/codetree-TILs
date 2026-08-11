T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

# Please write your code here.
s, n = [], []
answer = 0

for i in range(T):
    if c[i] == "S":
        s.append(x[i])
    else:
        n.append(x[i])

for k in range(a, b + 1):
    d1 = min(abs(pos - k) for pos in s)
    d2 = min(abs(pos - k) for pos in n)

    if d1 <= d2:
        answer += 1

print(answer)