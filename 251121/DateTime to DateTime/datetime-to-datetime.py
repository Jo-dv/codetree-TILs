a, b, c = map(int, input().split())

# Please write your code here.
start = 11 * 24 * 60 + 11 * 60 + 11
end = a * 24 * 60 + b * 60 + c
result = end - start
print(result if result >= 0 else -1)