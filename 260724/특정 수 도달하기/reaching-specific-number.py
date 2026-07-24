arr = list(map(int, input().split()))
temp = []

for i in arr:
    if i < 250:
        temp.append(i)
    else:
        break

print(sum(temp), round(sum(temp) / len(temp), 1))