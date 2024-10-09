class Main:
    def __init__(self):
        self.n, self.m, self.k = map(int, input().split())
        self.maze = [list(map(int, input().split())) for _ in range(self.n)]
        self.people = [list(map(lambda x:int(x) - 1, input().split())) for _ in range(self.m)]
        self.exit_y, self.exit_x = map(lambda x:int(x) - 1, input().split())
        self.rest_people = self.m
        self.answer = 0

    def init_maze(self):
        for y, x in self.people:
            self.maze[y][x] -= 1  # 같은 좌표인 사람들이 있음

        self.maze[self.exit_y][self.exit_x] = -99
        
    def move(self):
        arrive = [i[:] for i in self.maze]  # 이동할 임시 미로

        for y in range(self.n):
            for x in range(self.n):
                if -99 < self.maze[y][x] < 0:  # 사람인 경우
                    min_distance = abs(self.exit_y - y) + abs(self.exit_x - x)  # 현재 위치에서 탈출구까지

                    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        my = y + dy
                        mx = x + dx
                        distance = abs(self.exit_y - my) + abs(self.exit_x - mx)
                        if 0 <= my < self.n and 0 <= mx < self.n and self.maze[my][mx] <= 0 and distance < min_distance:
                            arrive[y][x] -= self.maze[y][x]  # 인원 이동
                            self.answer += (-self.maze[y][x])  # 인원한 이동 = 이동 횟수, 3명이면 3만큼의 이동 거리 발생
                            if arrive[my][mx] == -99:
                                self.rest_people -= (-self.maze[y][x])  # 인원 탈출, 값 자체가 음수이므로
                            else:
                                arrive[my][mx] += self.maze[y][x]  # 값 자체가 음수이므로
                            break  # 해당 인원 이동 종료

        self.maze = arrive
    
    def find_rect(self):
        min_len = self.n  # 사각형의 길이
        for y in range(self.n):
            for x in range(self.n):
                if -99 < self.maze[y][x] < 0:
                    min_len = min(min_len, max(abs(self.exit_y - y), abs(self.exit_x - x)))

        for ey in range(self.n - min_len):
            for ex in range(self.n - min_len):
                if ey <= self.exit_y <= ey + min_len and ex <= self.exit_x <= ex + min_len:
                    for py in range(ey, ey + min_len + 1):
                        for px in range(ex, ex + min_len + 1):
                            if -99 < self.maze[py][px] < 0:
                                return ey, ex, min_len + 1  # 좌측 상단을 기준으로 하니까

    def renew_exit(self):
        for y in range(self.n):
            for x in range(self.n):
                if self.maze[y][x] == -99:
                    return y, x

    def rotate(self):
        sy, sx, rect_len = self.find_rect()

        done = [i[:] for i in self.maze]
        for y in range(rect_len):
            for x in range(rect_len):
                done[y + sy][x + sx] = self.maze[rect_len - 1 - x + sy][y + sx]
                if done[y + sy][x + sx] > 0:
                    done[y + sy][x + sx] -= 1

        self.maze = done
        self.exit_y, self.exit_x = self.renew_exit()

    def solve(self):
        self.init_maze()  # 미로 초기화
        
        for step in range(1, self.k + 1):
            self.move()
            if self.rest_people == 0:  # 이동 후, 모든 인원이 다 탈출했다면 종료
                break

            self.rotate()

        print(self.answer)
        print(self.exit_y + 1, self.exit_x + 1)




problem = Main()
problem.solve()