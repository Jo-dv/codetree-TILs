N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.
answer = ""
status = [0] * (N+1)
status[P] = 1
table = [0] * (N+1)
table[P] = K

handshakes.sort(lambda i: i[0])

for t, x, y in handshakes:
    if status[x]:
        if table[x] > 0:
            if not status[y]:
                status[y] = 1
                table[y] = K
            else:
                if table[y] > 0:
                    table[y] -= 1
            table[x] -= 1

print(answer.join(str(i) for i in status[1:]))