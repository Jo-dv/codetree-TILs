n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
for i in arr:
    print(i // 2 if i % 2 == 0 else i, end=' ')