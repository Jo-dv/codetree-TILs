class Main:
    def __init__(self):
        self.n, self.m, self.k = map(int, input().split())
        self.grid = [[-1] * (self.n + 2)] + \
                    [[-1] + list(map(int, input().split())) + [-1] for _ in range(self.n)] + \
                    [[-1] * (self.n + 2)]
        self.players = [[0] * 4] + [list(map(int, input().split())) for _ in range(self.m)]
        self.points = [0] * (self.m + 1)
        self.gun = [0] * (self.m + 1)
        self.gun_grid = [[[] for _ in range(self.n + 2)] for _ in range(self.n + 2)]
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def init_grid(self):
        for y in range(1, self.n + 1):
            for x in range(1, self.n + 1):
                if self.grid[y][x] > 0:
                    self.gun_grid[y][x] = [self.grid[y][x]]

    def move_lose(self, loser):
        y, x, d, s = self.players[loser]

        for _ in range(4):
            dy, dx = self.directions[d]
            my, mx = y + dy, x + dx
            if not (1 <= my <= self.n and 1 <= mx <= self.n) or [i for i in self.players if i[:2] == [my, mx]]:
                d = (d + 1) % 4
            else:
                self.players[loser] = [my, mx, d, s]
                if len(self.gun_grid[my][mx]) > 0:
                    put_gun = self.gun[loser]
                    self.gun_grid[my][mx].sort()
                    self.gun[loser] = self.gun_grid[my][mx].pop()
                    if put_gun:
                        self.gun_grid[my][mx].append(put_gun)
                break

    def after_fight(self, winner, loser, y, x):
        if self.gun[loser] != 0:
            self.gun_grid[y][x].append(self.gun[loser])
            self.gun[loser] = 0  # 패자는 총 버림
            self.gun_grid[y][x].sort()
        self.move_lose(loser)  # 패자 이동

        if len(self.gun_grid[y][x]) > 0 and self.gun[winner] < self.gun_grid[y][x][-1]:  # 바닥에 총이 내거보다 좋으면 교환
            put_gun = self.gun[winner]
            self.gun[winner] = self.gun_grid[y][x].pop()
            self.gun_grid[y][x].append(put_gun)
            self.gun_grid[y][x].sort()
            # 소트

    def fight(self, player, enemy, y, x):
        player_atk = self.players[player][3] + self.gun[player]
        enemy_atk = self.players[enemy][3] + self.gun[enemy]
        if player_atk > enemy_atk:  # 주인공 승리
            self.points[player] += abs(player_atk - enemy_atk)
            self.after_fight(player, enemy, y, x)
        elif player_atk == enemy_atk:
            if self.players[player][3] > self.players[enemy][3]:  # 주인공 승리
                self.points[player] += abs(player_atk - enemy_atk)
                self.after_fight(player, enemy, y, x)
            elif self.players[player][3] < self.players[enemy][3]:  # 상대방 승리
                self.points[enemy] += abs(player_atk - enemy_atk)
                self.after_fight(enemy, player, y, x)
        else:  # 상대방 승리
            self.points[enemy] += abs(player_atk - enemy_atk)
            self.after_fight(enemy, player, y, x)

    def get_gun(self, player, my, mx):
        self.gun_grid[my][mx].sort()  # 가장 강한 총을 줍기 위해
        if len(self.gun_grid[my][mx]) > 0:  # 총이 바닥에 있고
            if self.gun[player] == 0:  # 내가 총이 없다면
                self.gun[player] = self.gun_grid[my][mx].pop()
            else:
                if self.gun[player] < self.gun_grid[my][mx][-1]:
                    put_gun = self.gun[player]
                    self.gun[player] = self.gun_grid[my][mx].pop()
                    self.gun_grid[my][mx].append(put_gun)

    def move(self):
        for player in range(1, self.m + 1):
            y, x, d, s = self.players[player]
            dy, dx = self.directions[d]
            my, mx = y + dy, x + dx
            if not (1 <= my <= self.n and 1 <= mx <= self.n):  # 벽에 부딪히면
                my, mx = y - dy, x - dx
                d = (d + 2) % 4
            self.players[player] = [my, mx, d, s]

            for enemy in range(1, self.m + 1):
                if player == enemy:  # 나는 범위에서 제외
                    continue
                if [my, mx] == self.players[enemy][:2]:  # 적이 있다면
                    self.fight(player, enemy, my, mx)
                    break
            else:  # 적이 없다면
                self.get_gun(player, my, mx)

    def solve(self):
        self.init_grid()
        for stage in range(1, self.k + 1):
            self.move()
            # print(self.gun[1:])
            # print(self.players)
            # print(*self.points[1:])

        print(*self.points[1:])


problem = Main()
problem.solve()