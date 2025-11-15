q = int(input())
commands = []
for _ in range(q):
    line = input().split()
    if line[0] != "clear":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0],))

# Please write your code here.
s = 0
for command in commands:
    if command[0] == "clear":
        s = 0;
    else:
        c, x = command
        if c == "add":
            if (s >> x) & 1 == 0:
                s += (1 << x)
        elif c == "delete":
            if (s >> x) & 1:
                s -= (1 << x)
        elif c == "print":
            print(1 if (s >> x) & 1 else 0)
        else:
            s ^= (1 << x)
