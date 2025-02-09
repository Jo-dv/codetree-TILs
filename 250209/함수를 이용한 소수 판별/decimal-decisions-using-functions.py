a, b = map(int, input().split())

# Write your code here!
def solve(a, b):
    answer = 0

    for i in range(a, b + 1):
        for j in range(2, a):
            if i % j == 0:
                break
        else:
            answer += i

    print(answer)
    return

solve(a, b)