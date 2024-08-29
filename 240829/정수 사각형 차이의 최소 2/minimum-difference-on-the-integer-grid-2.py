from math import inf

class Main():
    def __init__(self):
        self.n = int(input())
        self.arr = [list(map(int, input().split())) for _ in range(self.n)]
        self.dp = [[0] * self.n for _ in range(self.n)]
        self.answer = inf
                
    def search_upper(self, lower):
        for i in range(self.n):
            for j in range(self.n):
                if self.arr[i][j] < lower:
                    self.arr[i][j] = inf

        for i in range(self.n):
            for j in range(self.n):
                self.dp[i][j] = inf

        self.dp[0][0] = self.arr[0][0]

        for i in range(1, self.n):
            self.dp[0][i] = max(self.dp[0][i - 1], self.arr[0][i])

        for i in range(1, self.n):
            self.dp[i][0] = max(self.dp[i - 1][0], self.arr[i][0])

        for i in range(1, self.n):
            for j in range(1, self.n):
                self.dp[i][j] = max(min(self.dp[i - 1][j], self.dp[i][j - 1]), self.arr[i][j])

        return self.dp[-1][-1]
    
    def solve(self):
        for lower in range(1, 101):
            upper = self.search_upper(lower)

            if upper != inf:
                self.answer = min(self.answer, upper - lower)

        print(self.answer)

problem = Main()
problem.solve()