m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
date = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
day = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
cnt = 0

result = date[m1] - d1
for month in range(m1+1, m2):
    result += date[month]
result += d2

print(result, result // day[A])