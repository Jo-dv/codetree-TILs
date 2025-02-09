n = int(input())

# Write your code here!
def solve(depth):
    if depth == n:
        return
    solve(depth + 1)
    print("HelloWorld")

solve(0)