N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

# Please write your code here.
answer = 0
eat_list = {i: [] for i in range(1, M+1)}
for i in range(D):
    eat_list[m[i]].append([p[i], t[i]])

for cheese in range(1, M+1):
    candidate = True
    for sick_person, sick_time in zip(sick_p, sick_t):
        sick = False
        for person, time in eat_list[cheese]:
            if person == sick_person and time < sick_time:
                sick = True
                break
                
        if not sick:
            candidate = False
            break
        
    if candidate:
        people = set(p for p, t in eat_list[cheese])
        answer = max(answer, len(people))

print(answer)