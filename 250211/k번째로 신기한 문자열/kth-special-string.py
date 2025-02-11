n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Write your code here!
temp = [i for i in str if i[:len(t)] == t]
temp.sort()

print(temp[k - 1])