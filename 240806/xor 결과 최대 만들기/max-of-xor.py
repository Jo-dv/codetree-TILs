n, m = map(int, input().split())
num = list(map(int, input().split()))
selected_num = []
answer = 0

def back(idx, cnt):
    global answer
    if idx == n:
        if cnt == m:
            current = 0
            for i in selected_num:
                current ^= i
            answer = max(answer, current)
        return

    selected_num.append(num[idx])
    back(idx + 1, cnt + 1)
    selected_num.pop()
    back(idx + 1, cnt)

back(0, 0)
print(answer)