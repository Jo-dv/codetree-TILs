n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0
selected_lines = []

def search(idx):
    global answer
    
    if idx == n:
        for i, line1 in enumerate(selected_lines):
            for j, line2 in enumerate(selected_lines):
                if i < j and line1[0] <= line2[1] and line2[0] <= line1[1]:
                    return
        answer = max(answer, len(selected_lines))
        return

    selected_lines.append(lines[idx])    
    search(idx + 1)
    selected_lines.pop()
    search(idx + 1)

search(0)
print(answer)