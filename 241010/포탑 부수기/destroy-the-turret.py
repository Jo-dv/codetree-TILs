from collections import deque


class Main:
    def __init__(self):
        self.n, self.m, self.k = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.recent = [[0] * self.m for _ in range(self.n)]  # 마지막 공격 시점
        self.destroy = [[False] * self.m for _ in range(self.n)]  # 파괴된 포탑
        self.candidates = set()  # 회복 대상에서 제외할 포탑들
        self.answer = 0

    def init_game(self):  # 초기 부숴진 포탑 색출
        for y in range(self.n):
            for x in range(self.m):
                if self.grid[y][x] == 0:
                    self.destroy[y][x] = True

    def find_weak(self):  # 약한 포탑 탐색
        result = []
        min_atk = 5001
        for y in range(self.n):
            for x in range(self.m):
                if not self.destroy[y][x]:
                    if self.grid[y][x] <= min_atk:
                        min_atk = self.grid[y][x]
                        result.append((min_atk, self.recent[y][x], y + x, x, (y, x)))

        result.sort(key=lambda i: (i[0], -i[1], -i[2], -i[3]))
        return result[0][-1]  # 좌표만

    def find_strong(self):  # 강한 포탑 탐색
        result = []
        max_atk = 0
        for y in range(self.n):
            for x in range(self.m):
                if not self.destroy[y][x]:
                    if self.grid[y][x] >= max_atk:
                        max_atk = self.grid[y][x]
                        result.append((max_atk, self.recent[y][x], y + x, x, (y, x)))

        result.sort(key=lambda i: (-i[0], i[1], i[2], i[3]))
        return result[0][-1]  # 좌표만

    def attack(self, step):  # 모든 포탑 탐색 후, 공격
        self.candidates = set()  # 새로운 공격이 수행될 때마다 초기화
        atk_y, atk_x = self.find_weak()
        def_y, def_x = self.find_strong()

        self.grid[atk_y][atk_x] += (self.n + self.m)  # 공격력 보정
        self.recent[atk_y][atk_x] = step  # 공격 시점 갱신

        damage = self.grid[atk_y][atk_x]  # 편의를 위한 공격력 변수
        self.candidates.add((atk_y, atk_x))
        self.candidates.add((def_y, def_x))

        if not self.leaser(atk_y, atk_x, def_y, def_x, damage):
            self.bomb(atk_y, atk_x, def_y, def_x, damage)

    def leaser(self, atk_y, atk_x, def_y, def_x, damage):
        visited = [[[] for _ in range(self.m)] for _ in range(self.n)]
        dq = deque([(atk_y, atk_x)])
        visited[atk_y][atk_x] = (atk_y, atk_x)

        while dq:
            y, x = dq.popleft()
            if (y, x) == (def_y, def_x):
                self.grid[y][x] = max(0, self.grid[y][x] - damage)
                while True:
                    y, x = visited[y][x]
                    if (y, x) == (atk_y, atk_x):
                        return True
                    self.grid[y][x] = max(0, self.grid[y][x] - (damage // 2))
                    self.candidates.add((y, x))

            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                my, mx = (y + dy) % self.n, (x + dx) % self.m
                if not self.destroy[my][mx] and not visited[my][mx]:
                    visited[my][mx] = (y, x)
                    dq.append((my, mx))

        return False

    def bomb(self, atk_y, atk_x, def_y, def_x, damage):
        y, x = def_y, def_x
        self.grid[y][x] = max(0, self.grid[y][x] - damage)
        for dy, dx in ((0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
            my, mx = (y + dy) % self.n, (x + dx) % self.m
            if (my, mx) == (atk_y, atk_x):  # 자기 자신은 범위에서 제외
                continue
            self.grid[my][mx] = max(0, self.grid[my][mx] - (damage // 2))
            self.candidates.add((my, mx))

    def check_destroy(self):
        for y in range(self.n):
            for x in range(self.m):
                if self.grid[y][x] == 0:
                    self.destroy[y][x] = True

    def recover(self):  # 무관한 포탑 회복
        for y in range(self.n):
            for x in range(self.m):
                if (y, x) not in self.candidates and not self.destroy[y][x]:
                    self.grid[y][x] += 1

    def check_terminate(self):
        tower = self.n * self.m
        for y in range(self.n):
            for x in range(self.m):
                if self.destroy[y][x]:
                    tower -= 1

        return True if tower <= 1 else False  # 남은 타워가 하나 이하라면

    def solve(self):
        self.init_game()

        for step in range(1, self.k + 1):
            self.attack(step)
            self.check_destroy()
            if self.check_terminate():
                break
            self.recover()

        for i in self.grid:
            self.answer = max(self.answer, max(i))

        print(self.answer)


problem = Main()
problem.solve()