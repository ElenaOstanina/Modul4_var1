from math import inf


def divide(first, second):
    if second == 0:
        result = inf

    else:
        result = first / second

    print(result)

    return result
