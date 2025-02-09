N = int(input())

# Write your code here!
def solve(num, depth):
    if depth == N + 1:
        print(num)
        return
    solve(num + depth, depth + 1)

solve(0, 0) 