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
        self.total_damage = [0] * (self.n + 1)
        self.answer = 0

    def move(self, i, d):
        current_damage = [0] * (self.n + 1)
        dq = deque([i])
        checked = {i}

        while dq:
            current = dq.popleft()
            y, x, h, w, k = self.knights[current]
            dy, dx = self.directions[d]
            sy = y + dy
            sx = x + dx

            for my in range(sy, sy + h):  # 방패를 들고 이동
                for mx in range(sx, sx + w):
                    if self.board[my][mx] == 2:
                        return
                    if self.board[my][mx] == 1 and current != i:  # 원래 기사가 아니라면, 그에 의해 밀린 기사들
                        current_damage[current] += 1  # 받은 데미지

            for knight in self.knights:  # 기사들의
                if knight not in checked:  # 이동 여부 파악
                    ty, tx, th, tw, tk = self.knights[knight]
                    if sy + h - 1 >= ty and ty + th - 1 >= sy and sx + w - 1 >= tx and tx + tw - 1 >= sx:  # 겹쳐서 이동
                        checked.add(knight)  # 현재 이동에서 중복으로 밀지 않기 위해
                        dq.append(knight)  # 이동을 위해 다음 큐에 저장

        for knight in checked:  # 이동이 된 기사들 중에
            y, x, _, _, k = self.knights[knight]
            if k <= current_damage[knight]:  # 체력이 떨어졌다면
                self.knights.pop(knight)
            else:  # 이동 정보 갱신
                dy, dx = self.directions[d]
                self.knights[knight][0] = y + dy
                self.knights[knight][1] = x + dx
                self.knights[knight][4] -= current_damage[knight]
                self.total_damage[knight] += current_damage[knight]  # 전체 누적 데미지

    def solve(self):
        for cmd in self.command:
            knight, d = cmd
            if knight in self.knights:
                self.move(knight, d)

        for i in self.knights:  # 남은 기사들 중 받은 데미지
            self.answer += self.total_damage[i]

        print(self.answer)


problem = Main()
problem.solve()