from collections import deque


class Main:
    def __init__(self):
        self.k, self.m = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(5)]
        self.nums = deque(list(map(int, input().split())))

    def is_valid(self, y, x):
        return 0 <= y < 5 and 0 <= x < 5

    def rotate(self, y, x, cnt):  # 격자 회전
        rotated_grid = [i[:] for i in self.grid]
        for _ in range(cnt):
            temp = rotated_grid[y][x + 2]
            rotated_grid[y][x + 2] = rotated_grid[y][x]
            rotated_grid[y][x] = rotated_grid[y + 2][x]
            rotated_grid[y + 2][x] = rotated_grid[y + 2][x + 2]
            rotated_grid[y + 2][x + 2] = temp
            temp = rotated_grid[y][x + 1]
            rotated_grid[y][x + 1] = rotated_grid[y + 1][x]
            rotated_grid[y + 1][x] = rotated_grid[y + 2][x + 1]
            rotated_grid[y + 2][x + 1] = rotated_grid[y + 1][x + 2]
            rotated_grid[y + 1][x + 2] = temp
        return rotated_grid

    def calculate(self, rotated):  # 유물 점수 계산
        score = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * 5 for _ in range(5)]

        for i in range(5):
            for j in range(5):
                if not visited[i][j]:
                    dq = deque([(i, j)])
                    cnt = deque([(i, j)])
                    visited[i][j] = True

                    while dq:
                        y, x = dq.popleft()
                        for dy, dx in directions:
                            my = y + dy
                            mx = x + dx
                            if self.is_valid(my, mx) and not visited[my][mx] and rotated[y][x] == rotated[my][mx]:
                                visited[my][mx] = True
                                dq.append((my, mx))
                                cnt.append((my, mx))

                    if len(cnt) >= 3:
                        score += len(cnt)
                        while cnt:
                            y, x = cnt.popleft()
                            rotated[y][x] = 0

        return score

    def fill(self, rotate):  # 유물 채우기
        for x in range(5):
            for y in range(4, -1, -1):
                if rotate[y][x] == 0:
                    rotate[y][x] = self.nums.popleft()

    def solve(self):
        for i in range(self.k):
            max_score = 0
            find = None
            for cnt in range(1, 4):
                for x in range(3):
                    for y in range(3):
                        rotated = self.rotate(y, x, cnt)
                        score = self.calculate(rotated)
                        if max_score < score:
                            max_score = score
                            find = rotated
                        # 1. max_score를 통해 가치 최대화
                        # 2. 적은 각도부터 항상 시작하므로 동일 스코어가 나와도 갱신 안 함
                        # 3. 좌표의 열이 작으려면 행부터 검사, 열이 같은 경우를 대비해 위에서부터 검사해 행이 작은 구간 확보

            if find is None:  # 유물 못 찾았으면 종료 -> 점수 갱신이 없었다는 뜻
                break

            while True:
                self.fill(find)
                additional_score = self.calculate(find)

                if additional_score == 0:
                    break
                max_score += additional_score
            self.grid = find  # 다음 탐색에서 이어서 진행해야 함
            print(max_score, end=' ')


problem = Main()
problem.solve()