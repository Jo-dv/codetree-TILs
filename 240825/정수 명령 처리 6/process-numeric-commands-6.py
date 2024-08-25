import heapq

n = int(input())
cmd = [input().split() for _ in range(n)]
hq = []

for c in cmd:
    if c[0] == "push":
        heapq.heappush(hq, (-int(c[1]), int(c[1])))
    elif c[0]  == "pop":
        print(heapq.heappop(hq)[1])
    elif c[0] == "size":
        print(len(hq))
    elif c[0] == "empty":
        print(0 if len(hq) else 1)
    else:
        print(hq[0][1])