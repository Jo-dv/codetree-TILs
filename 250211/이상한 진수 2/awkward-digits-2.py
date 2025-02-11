a = input()

# Write your code here!
answer = 0
num = list(a)
for i in range(len(num)):
    origin = num[i]
    if num[i] == '0':
        num[i] = '1'
    else:
        num[i] = '0'
    answer = max(answer, int("".join(num), 2))
    num[i] = origin

print(answer)