import re
boxes = re.findall("(\d+)x(\d+)x(\d+)", open("day2.txt", 'r').read())
boxes = list(map(lambda x: [int(x[0]), int(x[1]), int(x[2])], boxes))
print(boxes)
def min_perimeter(x):
    m = min(x)
    x2 = x[:]
    x2.remove(m)
    m2 = min(x2)
    return m*2+m2*2


def volume(x):
    return x[0]*x[1]*x[2]


sum(map(min_perimeter, boxes))

print(sum(map(min_perimeter, boxes)) + sum(map(volume, boxes)))