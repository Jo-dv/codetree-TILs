n = int(input())

# Write your code here!
result = []

while n > 0:
    result.append(n % 2)
    n //= 2

for i in range(len(result) - 1, -1, -1):
    print(result[i], end='')