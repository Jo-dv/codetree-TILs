m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
date = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
if m1 == m2:
    print(d2 - d1)
else:
    temp = date[m1] - d1 + 1
    for month in range(m1+1, m2):
        temp += date[month]
    temp += d2
    print(temp)