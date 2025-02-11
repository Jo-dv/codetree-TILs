n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# Write your code here!
a = set(a)
b = set(b)
for i in b:
    print(1 if i in a else 0)