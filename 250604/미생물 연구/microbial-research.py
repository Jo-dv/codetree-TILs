from collections import deque


class Main:
    def __init__(self):
        self.n, self.q = map(int, input().split())
        self.cells = [tuple(map(int, input().split())) for _ in range(self.q)]
        self.grid = [[0] * self.n for _ in range(self.n)]
        self.answer = []
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.info = {i: [] for i in range(1, self.q + 1)}

    def is_valid(self, y, x):
        return 0 <= y < self.n and 0 <= x < self.n

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
                    visited[y][x] = True

                    while dq:
                        cy, cx = dq.popleft()
                        for dy, dx in self.directions:
                            my, mx = cy + dy, cx + dx
                            if self.is_valid(my, mx) and self.grid[my][mx] == cell and not visited[my][mx]:
                                dq.append((my, mx))
                                visited[my][mx] = True

                    check[cell] += 1

        for cell in range(1, self.q + 1):
            if check[cell] >= 2:
                self.info[cell] = []

    def inject_cell(self, cell, num):
        r1, c1, r2, c2 = cell

        current = []
        for r in range(r1, r2):
            for c in range(c1, c2):
                check = self.grid[r][c]
                if check != 0 and check != num:
                    self.info[check].remove((r, c))
                self.grid[r][c] = num
                current.append((r, c))

        self.check_split(num)
        self.info[num] = current

    def move_cell(self):
        standards = sorted(self.info.items(), key=lambda i: (-len(i[1]), i[0]))
        new_grid = [[0] * self.n for _ in range(self.n)]

        for standard in standards:
            num, cells = standard

            if cells:
                min_y, min_x, max_y, max_x = self.n + 1, self.n + 1, 0, 0
                for y in range(self.n):
                    for x in range(self.n):
                        if self.grid[y][x] == num:
                            min_y = min(min_y, y)
                            min_x = min(min_x, x)
                            max_y = max(max_y, y)
                            max_x = max(max_x, x)

                width = max_x - min_x + 1
                height = max_y - min_y + 1

                for y in range(self.n - height + 1):
                    can_y = False
                    for x in range(self.n - width + 1):
                        can_x = True
                        for dy in range(height):
                            for dx in range(width):
                                origin_y = min_y + dy
                                origin_x = min_x + dx
                                if self.grid[origin_y][origin_x] != num:
                                    continue
                                if new_grid[y + dy][x + dx] != 0:
                                    can_x = False
                                    break
                            if not can_x:
                                break

                        if can_x:
                            new_cord = []
                            for dy in range(height):
                                for dx in range(width):
                                    origin_y = min_y + dy
                                    origin_x = min_x + dx
                                    if self.grid[origin_y][origin_x] != num:
                                        continue
                                    new_grid[y + dy][x + dx] = num
                                    new_cord.append((y + dy, x + dx))
                            can_y = True
                            self.info[num] = new_cord
                            break
                    if can_y:
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
            self.inject_cell(self.cells[i], i + 1)
            self.move_cell()
            self.get_result()

        for i in self.answer:
            print(i)


problem = Main()
problem.solve()
