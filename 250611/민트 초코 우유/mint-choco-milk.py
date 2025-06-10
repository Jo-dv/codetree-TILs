from collections import deque

class Main:
    def __init__(self):
        self.n, self.t = map(int, input().split())
        self.food = [input() for _ in range(self.n)]
        self.believe = [list(map(int, input().split())) for _ in range(self.n)]
        self.answer = []

    def preprocessing(self):
        bit_food = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if self.food[i][j] == "T":
                    bit_food[i][j] = 4
                elif self.food[i][j] == "C":
                    bit_food[i][j] = 2
                else:
                    bit_food[i][j] = 1

        self.food = bit_food

    def is_valid(self, y, x):
        return 0 <= y < self.n and 0 <= x < self.n

    def morning(self):
        for i in range(self.n):
            for j in range(self.n):
                self.believe[i][j] += 1

    def lunch(self):
        self.food: list[[int]]
        visited = [[False] * self.n for _ in range(self.n)]
        one = []
        two = []
        three = []

        for i in range(self.n):
            for j in range(self.n):
                if not visited[i][j]:
                    dq = deque([(i, j)])
                    visited[i][j] = True
                    believe_point = self.believe[i][j]  # 대표의 신앙심
                    by, bx = i, j  # 대표의 위치
                    believer = [(by, bx)]  # 현 그룹의 속한 학생들
                    target_food = self.food[i][j]  # 현 그룹의 음식

                    while dq:
                        y, x = dq.popleft()

                        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            my, mx = y + dy, x + dx
                            if self.is_valid(my, mx) and not visited[my][mx] and self.food[my][mx] == target_food:
                                dq.append((my, mx))
                                visited[my][mx] = True
                                believer.append((my, mx))
                                if believe_point < self.believe[my][mx]:
                                    believe_point = self.believe[my][mx]
                                    by = my
                                    bx = mx

                    self.believe[by][bx] += (len(believer) - 1)
                    for y, x in believer:
                        if (y, x) == (by, bx):
                            continue
                        self.believe[y][x] -= 1

                    if self.food[by][bx] in [4, 2, 1]:
                        one.append((self.believe[by][bx], by, bx))
                    elif self.food[by][bx] in [6, 5, 3]:
                        two.append((self.believe[by][bx], by, bx))
                    else:
                        three.append((self.believe[by][bx], by, bx))

        one.sort(key=lambda i: (-i[0], i[1], i[2]))
        two.sort(key=lambda i: (-i[0], i[1], i[2]))
        three.sort(key=lambda i: (-i[0], i[1], i[2]))
        return one, two, three

    def evening(self, one, two, three):
        self.food: list[[int]]
        groups = [one, two, three]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * self.n for _ in range(self.n)]

        for group in groups:
            for current in group:
                believe, y, x = current
                if visited[y][x]:
                    continue
                target_food = self.food[y][x]
                energy = believe - 1
                self.believe[y][x] = 1
                d = believe % 4
                cy, cx = y, x

                while True:
                    cy += directions[d][0]
                    cx += + directions[d][1]
                    if cy < 0 or cy >= self.n or cx < 0 or cx >= self.n or energy == 0:
                        break

                    if self.food[cy][cx] == target_food:
                        continue

                    if energy > self.believe[cy][cx]:
                        energy -= (self.believe[cy][cx] + 1)
                        self.believe[cy][cx] += 1
                        self.food[cy][cx] = target_food
                        visited[cy][cx] = True
                    else:
                        self.believe[cy][cx] += energy
                        self.food[cy][cx] |= target_food
                        visited[cy][cx] = True
                        break

    def cal_believe(self):
        self.food: list[list[int]]
        result = [0] * 7
        table = {7: 0, 6: 1, 5: 2, 3: 3, 1: 4, 2: 5, 4: 6}
        for i in range(self.n):
            for j in range(self.n):
                food = table[self.food[i][j]]
                result[food] += self.believe[i][j]

        self.answer.append(result)

    def solve(self):
        self.preprocessing()

        for _ in range(self.t):
            self.morning()
            one, two, three = self.lunch()
            self.evening(one, two, three)
            self.cal_believe()

        for i in self.answer:
            print(*i)


problem = Main()
problem.solve()