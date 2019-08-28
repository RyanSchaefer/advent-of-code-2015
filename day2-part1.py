import re
boxes = re.findall("(\d+)x(\d+)x(\d+)", open("day2.txt", 'r').read())
boxes = list(map(lambda x: (int(x[0]), int(x[1]), int(x[2])), boxes))
boxes = list(map(lambda x: (x[0]*x[1], x[1]*x[2], x[2]*x[0]), boxes))
boxes = list(
    map(
        lambda x:
        2*x[0] +
        2*x[1] +
        2*x[2] +
        min(x), boxes))
print(sum(boxes))
