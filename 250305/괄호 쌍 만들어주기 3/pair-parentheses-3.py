A = input()

# Please write your code here.
answer = 0

for i in range(len(A) - 1):
    if A[i] == ')':
        continue
    for j in range(i + 1, len(A)):
        if A[j] == ')':
            answer += 1

print(answer)