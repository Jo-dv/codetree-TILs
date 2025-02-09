n = int(input())

# Write your code here!
num = 1
for _ in range(n):
    for _ in range(n):
        print(num, end=' ')
        num = 1 if num > 8 else num + 1
    print()