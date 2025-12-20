N = int(input())
a = list(input())
b = list(input())

# Please write your code here.
answer = 0
flag = False

while a:
    if a[-1] == b[-1]:
        flag = False
    else:
        if not flag:
            answer += 1
            flag = True
    a.pop()
    b.pop()

print(answer)