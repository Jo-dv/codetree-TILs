from collections import deque

class Main:
    def __init__(self):
        self.l, self.n, self.q = map(int, input().split())
        self.board = [[2] * (self.l + 2)] + [
            [2] + list(map(int, input().split())) + [2] for _ in range(self.l)
        ] + [[2] * (self.l + 2)] # 0: 빈칸, 1: 함정, 2: 벽
        self.knights = {i: list(map(int, input().split())) for i in range(1, self.n + 1)}  # r, c, h, w, k
        self.command = [list(map(int, input().split())) for _ in range(self.q)]  # i, d
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.damage = [0] * (self.n + 1)
        self.answer = 0

    def move(self, i, d):
        dq = deque([i])
        checked = {i}

        while dq:
            current = dq.popleft()
            y, x, h, w, k = self.knights[current]
            dy, dx = self.directions[d]
            sy = y + dy
            sx = x + dx

            for my in range(sy, sy + h):
                for mx in range(sx, sx + w):
                    if self.board[my][mx] == 2:
                        return
                    if self.board[my][mx] == 1 and current != i:  # 미는 기사가 아니라면
                        self.knights[current][4] -= 1  # 체력 감소
                        self.damage[current] += 1  # 받은 데미지

            for knight in self.knights:
                if knight not in checked:
                    ty, tx, th, tw, tk = self.knights[knight]
                    if sy + h - 1 >= ty and ty + th - 1 >= sy and sx + w - 1 >= tx and tx + tw - 1 >= sx:
                        checked.add(knight)
                        dq.append(knight)

        for knight in checked:
            y, x, _, _, k = self.knights[knight]
            if k <= 0:
                self.knights.pop(knight)
            else:
                dy, dx = self.directions[d]
                self.knights[knight][0] = y + dy
                self.knights[knight][1] = x + dx

    def solve(self):
        for cmd in self.command:
            knight, d = cmd
            if knight in self.knights:
                self.move(knight, d)

        for i in self.knights:  # 남은 기사들 중 받은 데미지
            self.answer += self.damage[i]

        print(self.answer)


problem = Main()
problem.solve()