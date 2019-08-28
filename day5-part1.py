filter1 = lambda x: sum([x.count(y) for y in "aeiou"]) >= 3
filter2 = lambda x: any([y[0] == y[1] for y in zip(x[:-1], x[1:])])
filter3 = lambda x: all([s not in x for s in ["ab", "cd", "pq", "xy"]])

print(len(list(filter(filter1, filter(filter2, filter(filter3, open("day5.txt", 'r').readlines()))))))