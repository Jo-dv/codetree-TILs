N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
info = [0] * (N + 1)

for i in student:
    info[i] += 1
    if info[i] >= K:
        print(i)
        break
else:
    print(-1)