binary = input()

# Write your code here!
answer = 0

for i in range(len(binary)-1, -1, -1):
    answer += (int(binary[-i-1]) * 2**i)

print(answer)