n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

# Write your code here!

hashmap = dict()

for c in commands:
    if c[0] == "add":
        hashmap[c[1]] = c[2]
    elif c[0] == "remove":
        hashmap.pop(c[1])
    else:
        if c[1] in hashmap:
            print(hashmap[c[1]])
        else:
            print(None)