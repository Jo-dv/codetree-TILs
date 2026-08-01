n = int(input())
pointers = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        if i != j:
            for k in range(n):
                if i != k and j != k:
                    pointer1, pointer2, pointer3 = pointers[i], pointers[j], pointers[k]
                    if pointer1[1] == pointer2[1] and pointer1[0] == pointer3[0]:
                        width = abs(pointer1[0] - pointer2[0])
                        height = abs(pointer1[1] - pointer3[1])
                        answer = max(answer, width * height)

print(answer)