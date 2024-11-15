from collections import deque

class Main:
    def __init__(self):
        self.n, self.m, self.p, self.c, self.d = map(int, input().split())
        self.y, self.x = map(int, input().split())
        self.santas = [[0, 0] for _ in range(self.p + 1)]
        for _ in range(1, self.p + 1):
            santa, sy, sx = list(map(int, input().split()))
            self.santas[santa][0], self.santas[santa][1] = sy, sx
        self.board = [[0] * (self.n + 2) for _ in range(self.n + 2)]
        self.scores = [0] * (self.p + 1)  # 점수
        self.alive = [True] * (self.p + 1)  # 생존 여부
        self.stun = [0] * (self.p + 1)  # 기절 시간

    @staticmethod
    def cal_distance(r1, c1, r2, c2):
        return (r1 - r2)**2 + (c1 - c2)**2

    def find_santa(self):
        distances = []
        min_distance = 2 * self.n**2
        for santa in range(1, self.p + 1):  # 가장 가까운 산타 찾기
            if not self.alive[santa]:
                continue
            sy, sx = self.santas[santa]
            distance = self.cal_distance(self.y, self.x, sy, sx)
            if distance <= min_distance:
                min_distance = distance
                distances.append((min_distance, sy, sx, santa))
        distances.sort(key=lambda x: (x[0], -x[1], -x[2]))
        return distances[0]

    def move_rudolph(self, turn):
        closest_santa = self.find_santa()
        _, sy, sx, santa = closest_santa

        dy, dx = 0, 0
        if self.y < sy:
            dy = 1
        elif self.y > sy:
            dy = -1

        if self.x < sx:
            dx = 1
        elif self.x > sx:
            dx = -1

        self.board[self.y][self.x] = 0
        self.y, self.x = self.y + dy, self.x + dx
        self.board[self.y][self.x] = -1

        if self.y == sy and self.x == sx:  # 루돌프가 산타와 충돌
            self.back_santa(santa, sy, sx, dy, dx, self.c)  # 산타 밀기
            self.stun[santa] = turn + 2
            self.scores[santa] += self.c

    def back_santa(self, santa, sy, sx, dy, dx, toward):
        dq = deque([(santa, sy, sx, toward)])

        while dq:
            santa, sy, sx, toward = dq.popleft()
            my, mx = sy + (dy * toward), sx + (dx * toward)
            if 1 <= my <= self.n and 1 <= mx <= self.n:
                if self.board[my][mx] != 0:  # 빈칸이면
                    dq.append((self.board[my][mx], my, mx, 1))
                self.board[my][mx] = santa
                self.santas[santa] = [my, mx]
            else:  # 보드를 벗어나면
                self.alive[santa] = False
                return

    def move_santa(self, turn, santa):
        sy, sx = self.santas[santa]
        distances = []
        min_distance = self.cal_distance(self.y, self.x, sy, sx)

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            my, mx = sy + dy, sx + dx
            distance = self.cal_distance(self.y, self.x, my, mx)
            if 1 <= my <= self.n and 1 <= mx <= self.n and self.board[my][mx] <= 0 and distance < min_distance:
                min_distance = distance
                distances.append((my, mx, dy, dx))

        if len(distances) != 0:
            my, mx, dy, dx = distances[-1]  # 마지막으로 저장된 좌표가 가장 가까운 좌표(조건문상 계속 최소 거리일 때 활성화되므로)
            if my == self.y and mx == self.x:
                self.board[sy][sx] = 0
                self.back_santa(santa, my, mx, -dy, -dx, self.d)
                self.stun[santa] = turn + 2
                self.scores[santa] += self.d
            else:
                self.board[sy][sx] = 0
                self.board[my][mx] = santa
                self.santas[santa] = [my, mx]

    def init_board(self):
        self.alive[0] = False
        for santa in range(1, self.p + 1):  # 산타 위치
            sy, sx = self.santas[santa]
            self.board[sy][sx] = santa

        self.board[self.y][self.x] = -1

    def solve(self):
        self.init_board()
        # for i in self.board:
        #     print(i)
        # print()
        for turn in range(1, self.m + 1):
            if self.alive.count(True) == 0:
                break
            self.move_rudolph(turn)
            for santa in range(1, self.p + 1):
                if not self.alive[santa]:
                    continue
                if self.stun[santa] > turn:
                    continue
                self.move_santa(turn, santa)

            for santa in range(1, self.p + 1):
                if self.alive[santa]:
                    self.scores[santa] += 1

            # print(turn)
            # for i in self.board:  # 디버깅 코드
            #     print(i)
            # print()

        print(*self.scores[1:], end=' ')

problem = Main()
problem.solve()