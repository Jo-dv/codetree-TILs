n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.
while True:
    temp = []
    low = 0
    high = 0
    while high < len(numbers):
        if numbers[low] == numbers[high]:
            high += 1
        else:
            if high - low >= m:
                for i in range(low, high):
                    temp.append(i)
            low = high
            high += 1
    else:
        if high - low >= m:
            for i in range(low, high):
                temp.append(i)
    if not temp:
        break
    numbers = [numbers[i] for i in range(len(numbers)) if i not in temp]

print(len(numbers))
for i in numbers:
    print(i)