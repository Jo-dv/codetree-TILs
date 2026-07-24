exp = input().strip()

alphabets = sorted(set(ch for ch in exp if ch.isalpha()))
values = {}
answer = float("-inf")


def calculate():
    result = values[exp[0]]

    for i in range(1, len(exp), 2):
        operator = exp[i]
        number = values[exp[i + 1]]

        if operator == "+":
            result += number
        elif operator == "-":
            result -= number
        else:
            result *= number

    return result


def search(depth):
    global answer

    if depth == len(alphabets):
        answer = max(answer, calculate())
        return

    alphabet = alphabets[depth]

    for number in range(1, 5):
        values[alphabet] = number
        search(depth + 1)


search(0)
print(answer)