a, b = map(int, input().split())

# Write your code here!
def solve(a, b):
    answer = 0

    for i in range(a, b + 1):
        if i == 1:
            continue
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            answer += i

    print(answer)
    return

solve(a, b)
