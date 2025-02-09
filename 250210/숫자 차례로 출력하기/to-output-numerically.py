n = int(input())

# Write your code here!
def solve1(num, depth):
    if depth == n:
        return
    print(num, end=' ')
    solve1(num + 1, depth + 1)

def solve2(num, depth):
    if depth == 0:
        return
    print(num, end=' ')
    solve2(num - 1, depth - 1)

solve1(1, 0)
print()
solve2(n, n)