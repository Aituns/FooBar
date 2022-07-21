from imp import source_from_cache
from json.encoder import INFINITY

def solution(xs):

    result = 1
    
    if (len(xs) == 0):
        return xs[0]

    useful = []
    for i in xs:
        if i != 0:
            useful.append(i)
    
    negative = [i for i in useful if i < 0]
    negative = sorted(negative)
    positive = [j for j in useful if j > 0]

    if len(negative) == 0 and len(positive) == 0:
        return 0
    
    for i in positive:
        if i != 0:
            result = result * i
    
    if len(negative) % 2 == 0:
        for n in negative:
            result = result * n
    elif len(negative) == 1 and len(positive) == 0:
        result = result * negative[0]
    else:
        del negative[-1]
        for n in negative:
            result = result * n
            
    return str(result)

case0 = [2, 0, 2, 2, 0]
print("\nCase 0:\n ", case0, "\n\n  Expected: 8\nCalculated:", solution(case0))

case1 = [-2, -3, 4, -5]
print("\nCase 1:\n ", case1, "\n\n  Expected: 60\nCalculated:", solution(case1))

case2 = [0, 0, 0, -43]
print("\nCase 2:\n ", case2, "\n\n  Expected: -43\nCalculated:", solution(case2))

case3 = [0, 0]
print("\nCase 3:\n ", case3, "\n\n  Expected: 0\nCalculated:", solution(case3))

case4 = [0, 0, 4]
print("\nCase 4:\n ", case4, "\n\n  Expected: 4\nCalculated:", solution(case4))

case5 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
print("\nCase 5:\n ", case5, "\n\n  Expected: 1000000000000000000000000000000000000000000000000000000\
\nCalculated:", solution(case5))