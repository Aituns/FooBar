# Fuel Injection Projection

def solution(n):
    operations = 0

    isNotEqualToOne = True

    while (isNotEqualToOne):
        isEven = (n % 2 == 0)
        if (isEven):
            n = n / 2
        else:
            n = n - 1
        isNotEqualToOne = (n != 1)
        operations += 1
    return operations


print(solution(4))
