from collections import deque

class Main:
    def __init__(self):
        self.r, self.c, self.k = map(int, input().split())
        self.info = [tuple(map(int, input().split())) for _ in range(self.k)]
        self.grid = [[-1] + [0] * self.c + [-1] for _ in range(self.r + 3)] + [[-1] * (self.c + 2)]
        self.gate = [[False] * (self.c + 2) for _ in range(self.r + 4)]
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.answer = 0

    def down(self, y, x, d, golem):
        while True:
            # 남쪽 이동
            if self.grid[y + 1][x - 1] == self.grid[y + 2][x] == self.grid[y + 1][x + 1] == 0:
                y += 1
            # 서쪽 이동
            elif self.grid[y - 1][x - 1] == self.grid[y][x - 2] == self.grid[y + 1][x - 1] == self.grid[y + 1][x - 2] == self.grid[y + 2][x - 1] == 0:
                y += 1
                x -= 1
                d = (d - 1) % 4
            # 동쪽 이동
            elif self.grid[y - 1][x + 1] == self.grid[y][x + 2] == self.grid[y + 1][x + 1] == self.grid[y + 1][x + 2] == self.grid[y + 2][x + 1] == 0:
                y += 1
                x += 1
                d = (d + 1) % 4
            else:
                break

        # 골렘 세팅
        self.grid[y][x] = golem
        for dy, dx in self.directions:
            my = y + dy
            mx = x + dx
            self.grid[my][mx] = golem
        dy, dx = self.directions[d]
        self.gate[y + dy][x + dx] = True

        return y, x

    def clear(self):
        self.grid = [[-1] + [0] * self.c + [-1] for _ in range(self.r + 3)] + [[-1] * (self.c + 2)]
        self.gate = [[False] * (self.c + 2) for _ in range(self.r + 4)]

    def move(self, init_y, init_x):
        visited = [[False] * (self.c + 2) for _ in range(self.r + 4)]
        dq = deque([(init_y, init_x)])
        visited[init_y][init_x] = True
        deep_depth = 0

        while dq:
            y, x = dq.popleft()
            for dy, dx in self.directions:
                my = y + dy
                mx = x + dx
                if not visited[my][mx] and (self.grid[my][mx] == self.grid[y][x] or (0 < self.grid[my][mx] and self.gate[y][x])):
                    visited[my][mx] = True
                    dq.append((my, mx))
                    deep_depth = max(deep_depth, my - 3 + 1)  # 행이 1번부터 시작

        self.answer += deep_depth

    def solve(self):
        golem = 1
        for x, d in self.info:
            y, x = self.down(1, x, d, golem)
            golem += 1
            if y < 4:
                self.clear()
                continue
            self.move(y, x)

        print(self.answer)


problem = Main()
problem.solve()