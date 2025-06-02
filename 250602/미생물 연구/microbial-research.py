from collections import deque


class Main:
    def __init__(self):
        self.n, self.q = map(int, input().split())
        self.cells = [tuple(map(int, input().split())) for _ in range(self.q)]
        self.grid = [[0] * self.n for _ in range(self.n)]
        self.answer = []
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.info = {i: [] for i in range(1, self.q + 1)}

    def check_split(self, num):
        check = [0] * (self.q + 1)
        visited = [[False] * self.n for _ in range(self.n)]

        for y in range(self.n):
            for x in range(self.n):
                if self.grid[y][x] == num:
                    continue
                if self.grid[y][x] != 0 and not visited[y][x]:
                    dq = deque([(y, x)])
                    cell = self.grid[y][x]
                    while dq:
                        cy, cx = dq.popleft()
                        for dy, dx in self.directions:
                            my, mx = cy + dy, cx + dx
                            if 0 <= my < self.n and 0 <= mx < self.n and self.grid[my][mx] == cell and not visited[my][mx]:
                                dq.append((my, mx))
                                visited[my][mx] = True

                    check[cell] += 1

        for cell in range(1, self.q+1):
            if check[cell] > 1:
                self.info[cell] = []

    def inject_cell(self, cell, num):
        r1, c1, r2, c2 = cell

        current = []
        for r in range(r1, r2):
            for c in range(self.n - c2, self.n - c1):
                check = self.grid[c][r]
                if check != 0 and (c, r) in self.info[check]:
                    self.info[check].remove((c, r))
                self.grid[c][r] = num
                current.append((c, r))

        self.check_split(num)

        return current

    def move_cell(self):
        standards = sorted(self.info.items(), key=lambda i: (-len(i[1]), i[0]))
        new_grid = [[0] * self.n for _ in range(self.n)]

        for standard in standards:
            num, cells = standard

            if cells:
                flag = False
                max_y = max(cells, key=lambda cell: cell[0])[0]  # 가장 아래 y
                min_x = min(cells, key=lambda cell: cell[1])[1]  # 가장 왼쪽 x

                for x in range(self.n):  # 왼쪽부터 오른쪽으로
                    for y in range(self.n - 1, -1, -1):  # 아래에서 위로
                        if all(0 <= y - (max_y - cy) < self.n and 0 <= x + (cx - min_x) < self.n and new_grid[y - (max_y - cy)][x + (cx - min_x)] == 0 for cy, cx in cells):
                            new_cord = []
                            for cy, cx in cells:
                                ny = y - (max_y - cy)
                                nx = x + (cx - min_x)
                                new_grid[ny][nx] = num
                                new_cord.append((ny, nx))
                            self.info[num] = new_cord
                            flag = True
                            break
                    if flag:
                        break

        self.grid = new_grid

    def get_result(self):
        pairs = set()
        result = 0

        for y in range(self.n):
            for x in range(self.n):
                cell = self.grid[y][x]

                if cell != 0:
                    for dy, dx in self.directions:
                        my, mx = y + dy, x + dx
                        if 0 <= my < self.n and 0 <= mx < self.n:
                            adj_cell = self.grid[my][mx]
                            if adj_cell != 0 and adj_cell != cell:
                                pair = tuple(sorted((cell, adj_cell)))
                                if pair not in pairs:
                                    result += (len(self.info[cell]) * len(self.info[adj_cell]))
                                    pairs.add(pair)

        self.answer.append(result)

    def solve(self):
        for i in range(self.q):
            cell = self.cells[i]
            self.info[i+1] = self.inject_cell(cell, i+1)
            self.move_cell()
            self.get_result()

        for i in self.answer:
            print(i)


problem = Main()
problem.solve()
