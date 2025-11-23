N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
answer = 0
cnt = 0
prev_state = None

for i in range(N):
    current_state = arr[i] > 0
    if prev_state is not None and prev_state == current_state:
        cnt += 1
    else:
        prev_state = current_state
        cnt = 1
    answer = max(answer, cnt)

print(answer)