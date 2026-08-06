import sys

input = sys.stdin.readline

N, M, D, S = map(int, input().split())

# eat_records[치즈] = [(사람, 먹은 시각), ...]
eat_records = [[] for _ in range(M + 1)]

for _ in range(D):
    person, cheese, eat_time = map(int, input().split())
    eat_records[cheese].append((person, eat_time))

sick_records = []

for _ in range(S):
    person, sick_time = map(int, input().split())
    sick_records.append((person, sick_time))

answer = 0

# 각 치즈를 상한 치즈라고 가정
for bad_cheese in range(1, M + 1):
    possible = True

    # 아픈 모든 사람이 아프기 전에 이 치즈를 먹었는지 확인
    for sick_person, sick_time in sick_records:
        ate_before_sick = False

        for person, eat_time in eat_records[bad_cheese]:
            if person == sick_person and eat_time < sick_time:
                ate_before_sick = True
                break

        if not ate_before_sick:
            possible = False
            break

    if not possible:
        continue

    # 해당 치즈를 한 번이라도 먹은 사람 수
    people = set()

    for person, eat_time in eat_records[bad_cheese]:
        people.add(person)

    answer = max(answer, len(people))

print(answer)