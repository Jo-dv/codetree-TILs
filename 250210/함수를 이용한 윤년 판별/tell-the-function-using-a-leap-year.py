y = int(input())

# Write your code here!
def solve(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            print("false")
        else:
            print("true")
    else:
        print("false")

solve(y)