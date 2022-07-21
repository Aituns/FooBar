from functools import total_ordering


def solution(x, y):
    x = int(x)
    y = int(y)
    total = 0
    while (x > 1 or y > 1):
        if (x > y):
            total += 1
            x = x - y
        if (x < y):
            total += 1
            y = y - x

    return str(total)


print(solution(4, 7))
