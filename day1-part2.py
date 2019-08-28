from functools import reduce

def consume(sofar, xi):
    if sofar[0] == -1:
        return sofar
    if xi == "(":
        return (sofar[0] + 1, sofar[1] + 1)
    else:
        if sofar[0] - 1 == -1:
            return (sofar[0] -1, sofar[1])
        return (sofar[0] - 1, sofar[1] + 1)

print(reduce(consume, open("day1.txt", 'r').read(), (0, 1)))