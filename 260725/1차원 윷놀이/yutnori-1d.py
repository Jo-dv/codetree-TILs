n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
horses = [1] * k
answer = 0

def run(turn):
    global answer
    if turn == n:
        score = sum(horse == m for horse in horses)
        answer = max(answer, score)
        return

    for horse in range(k):
        origin = horses[horse]

        if horses[horse] < m:
            horses[horse] = min(m, horses[horse] + nums[turn])

        run(turn + 1)
        horses[horse] = origin

run(0)
print(answer)