n, t = map(int, input().split())
belt1 = list(map(int, input().split()))
belt2 = list(map(int, input().split()))
belt3 = list(map(int, input().split()))
belt = belt1 + belt2 + belt3

temp = belt3[-1]

for i in range(len(belt) - 1, 0, -1):
    belt[i] = belt[i - 1]

belt[0] = temp

for i in range(0, len(belt), 3):
    print(*belt[i:i + 3])