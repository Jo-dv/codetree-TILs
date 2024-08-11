n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0
selected_lines = []

def search(idx):
    global answer
    if n == 1:
        answer = 1
        return
    if idx == n:
        for i, line1 in enumerate(selected_lines):
            for j, line2 in enumerate(selected_lines):
                if j > i:
                    if line1[1] < line2[0] or line2[1] < line1[0]:  # 겹치지 않은 경우 
                        answer = max(answer, len(selected_lines))
                        return
                    else:
                        return

        return

    selected_lines.append(lines[idx])    
    search(idx + 1)
    selected_lines.pop()
    search(idx + 1)

search(0)
print(answer)