n, m, q = map(int, input().split())
building = [list(map(int, input().split())) for _ in range(n)]
r, d = input().split()
r = int(r) - 1
d = 1
# d == 1: L
# d == -1: R

def wind(r, d):
    if d == 1:
        temp = building[r][-1]
        for i in range(m - 1, 0, -1):
            building[r][i] = building[r][i - 1]
        building[r][0] = temp
    else:
        temp = building[r][0]
        for i in range(m - 1):
            building[r][i] = building[r][i + 1]
        building[r][-1] = temp

wind(r, d)

up_d = d
for i in range(r, 0, -1):
    for j in range(m):
        if building[i][j] == building[i - 1][j]:
            up_d *= -1
            wind(i - 1, up_d)
            break
down_d = d
for i in range(r, n - 1):
    for j in range(m):
        if building[i][j] == building[i + 1][j]:
            down_d *= -1
            wind(i + 1, down_d)
            break

for i in building:
    print(*i)