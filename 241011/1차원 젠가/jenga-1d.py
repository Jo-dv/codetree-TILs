n = int(input())
arr = [int(input()) for _ in range(n)]
s1, e1 = map(lambda x: int(x) - 1, input().split())
s2, e2 = map(lambda x: int(x) - 1, input().split())

for i in ((s1, e1), (s2, e2)):
    s, e = i
    temp = []
    for j in range(s, e + 1):
        arr[j] = 0
    for k in range(len(arr)):
        if arr[k] != 0:
            temp.append(arr[k])
    arr = temp

print(len(arr))
for i in arr:
    print(i)