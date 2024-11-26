import math
from collections import deque

class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.store = [[0, 0]] + [list(map(lambda x: int(x) - 1, input().split())) for _ in range(self.m)]
        self.people = [[-1, -1] for _ in range(self.m + 1)]
        self.arrive = [False] * (self.m + 1)
        self.directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        self.time = 0
    
    def connect(self, man):
        start_y, start_x = self.store[man]
        visited = [[0] * self.n for _ in range(self.n)]
        dq = deque([(start_y, start_x)])
        visited[start_y][start_x] = 1

        while dq:  # 베이스캠프로부터 갈 수 있는 거리들 계산
            y, x = dq.popleft()
            for dy, dx in self.directions:
                my = y + dy
                mx = x + dx
                if 0 <= my < self.n and 0 <= mx < self.n and not visited[my][mx] and self.grid[my][mx] != -1:
                    visited[my][mx] = visited[y][x] + 1
                    dq.append((my, mx))

        return visited  # 연결 정보 반환

    def find_store(self, man):
        step = self.connect(man)
        man_y, man_x = self.people[man]
        min_distance = float('inf')
        final_y, final_x = -1, -1

        for dy, dx in self.directions:
            my = man_y + dy
            mx = man_x + dx
            if 0 <= my < self.n and 0 <= mx < self.n and step[my][mx] and min_distance > step[my][mx]:
                min_distance = step[my][mx]
                final_y, final_x = my, mx

        self.people[man] = [final_y, final_x]
                
    def update(self):
        for i in range(1, self.m + 1):
            y, x = self.people[i]
            if [y, x] == self.store[i]:
                self.arrive[i] = True
                self.grid[y][x] = -1

    def find_base(self, man):
        step = self.connect(man)
        man_y, man_x = self.people[man]
        min_distance = float('inf')

        for y in range(self.n):
            for x in range(self.n):
                if step[y][x] and step[y][x] < min_distance and self.grid[y][x] == 1:
                    min_distance = step[y][x]
                    man_y, man_x = y, x

        self.people[man] = (man_y, man_x)
        self.grid[man_y][man_x] = -1  # 갈 수 없음 이제

    def simulation(self):
        for man in range(1, self.m + 1):
            if self.arrive[man] or self.people[man] == [-1, -1]:  # 이미 편의점에 도착했거나 아직 베이스캠프를 찾지 못했으면
                continue
            self.find_store(man)  # 최단 경로로 목표 편의점 탐색
        self.update()  # 모든 이동이 끝나고 상태 확인
        if self.time <= self.m:  # 아직 베이스켐프를 찾지 못했다면
            self.find_base(self.time)
                
    def check_done(self):
        for i in range(1, self.m + 1):
            if not self.arrive[i]:  # 아직 편의점에 도착 못 한 사람이 있다면
                return False
            
        return True

    def solve(self):
        while True:
            self.time += 1
            self.simulation()
            if self.check_done():
                break

        print(self.time)
        

problem = Main()
problem.solve()
# 문제의 핵심은 편의점 기준 모든 범위를 탐색, 탐색한 결과를 바탕으로 최단 거리 베이스캠프 위치 갱신, 이후 다시 수행하여 최단 경로 갱신