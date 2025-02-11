n = int(input())
sequence = list(map(int, input().split()))

# Write your code here!
# temp = [(i, data) for i, data in enumerate(sequence, 1)]
# temp.sort(key=lambda x: (x[1], x[0]))

# print(temp)

temp = [(data, i) for i, data in enumerate(sequence)]
answer = [0] * n
temp.sort()

for i, data in enumerate(temp, 1):
    answer[data[1]] = i

print(*answer)