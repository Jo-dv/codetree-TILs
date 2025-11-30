n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.
temp = []
for i in range(n):
    if s1-1 <= i <= e1-1:
        continue
    temp.append(blocks[i])

result = []
for i in range(len(temp)):
    if s2-1 <= i <= e2-1:
        continue
    result.append(temp[i])

print(len(result))
for i in result:
    print(i)