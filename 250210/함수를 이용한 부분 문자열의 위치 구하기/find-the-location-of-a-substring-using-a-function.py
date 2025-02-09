text = input()
pattern = input()

# Write your code here!
def solve(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            print(i)
            return
    else:
        print(-1)

solve(text, pattern)