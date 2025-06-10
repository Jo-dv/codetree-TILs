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
                    believe_point = self.believe[i][j]
                    by, bx = i, j
                    believer = [(by, bx)]
                    target_food = self.food[i][j]

                    while dq:
                        y, x = dq.popleft()

                        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            my, mx = y + dy, x + dx
                            if self.is_valid(my, mx) and not visited[my][mx] and self.food[my][mx] == target_food:
                                dq.append((my, mx))
                                visited[my][mx] = True
                                believer.append((my, mx))
                                if believe_point < self.believe[my][mx] or (believe_point == self.believe[my][mx] and by < my and bx < mx):
                                    believe_point = self.believe[my][mx]
                                    by = my
                                    bx = mx

                    believer.remove((by, bx))  # 대표자 제외
                    self.believe[by][bx] += len(believer)
                    for y, x in believer:
                        self.believe[y][x] -= 1

                    if self.food[by][bx] in [4, 2, 1]:
                        one.append((self.believe[by][bx], by, bx, believer))
                    elif self.food[by][bx] in [6, 5, 3]:
                        two.append((self.believe[by][bx], by, bx, believer))
                    else:
                        three.append((self.believe[by][bx], by, bx, believer))

        one.sort(key=lambda i: (-i[0], i[1], i[2]))
        two.sort(key=lambda i: (-i[0], i[1], i[2]))
        three.sort(key=lambda i: (-i[0], i[1], i[2]))
        return one, two, three

    def evening(self, one, two, three):
        self.food: list[[int]]
        groups = [one, two, three]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        check = set()

        for group in groups:
            for current in group:
                believe, y, x, _ = current
                if (y, x) in check:
                    continue
                target_food = self.food[y][x]
                energy = believe - 1
                self.believe[y][x] = 1
                d = believe % 4

                while True:
                    y += directions[d][0]
                    x += + directions[d][1]
                    if y < 0 or y >= self.n or x < 0 or x >= self.n or energy == 0:
                        break

                    if self.food[y][x] == target_food:
                        continue

                    if energy > self.believe[y][x]:
                        energy -= (self.believe[y][x] + 1)
                        self.believe[y][x] += 1
                        self.food[y][x] = target_food
                        check.add((y, x))
                    else:
                        self.believe[y][x] += energy
                        self.food[y][x] |= target_food
                        check.add((y, x))
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