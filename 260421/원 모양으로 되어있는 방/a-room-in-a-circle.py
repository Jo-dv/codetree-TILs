n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
answer = float('inf')

for i in range(n):
    total_distance = 0
    for j in range(n):
        distance = (n - i + j) % n
        total_distance += (distance * a[j])
    
    answer = min(answer, total_distance)

print(answer)