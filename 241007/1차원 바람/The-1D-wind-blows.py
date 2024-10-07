n, m, q = map(int, input().split())
building = [list(map(int, input().split())) for _ in range(n)]
command = [input().split() for _ in range(q)]

def wind(r, d):
    if d == 1:
        temp = building[r][-1]
        for c in range(m - 1, 0, -1):
            building[r][c] = building[r][c - 1]
        building[r][0] = temp
    else:
        temp = building[r][0]
        for c in range(m - 1):
            building[r][c] = building[r][c + 1]
        building[r][-1] = temp

for cmd in command:
    r, d = cmd
    r = int(r) - 1
    d = 1 if d == 'L' else - 1
    wind(r, d)

    up_d = d
    flag = False
    for i in range(r, 0, -1):
        for j in range(m):
            if building[i][j] == building[i - 1][j]:
                up_d *= -1
                wind(i - 1, up_d)
                flag = True
                break
        else:
            flag = False
        if not flag:
            break

    down_d = d
    flag = False
    for i in range(r, n - 1):
        for j in range(m):
            if building[i][j] == building[i + 1][j]:
                down_d *= -1
                wind(i + 1, down_d)
                flag = True
                break
        else:
            flag = False
        if not flag:
            break

for i in building:
    print(*i)