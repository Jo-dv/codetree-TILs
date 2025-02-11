n = int(input())
A = list(map(int, input().split()))

# Write your code here!
answer = float('inf')
for i in range(n):
    temp = 0
    for j in range(n):
        if i == j:
            continue
        temp += abs(i - j) * A[j]

    answer = min(answer, temp)

print(answer) 