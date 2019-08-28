filter1 = lambda x: any([x[i] == x[i+2] for i in range(len(x)) if i < len(x)-2])
filter2 = lambda x: any([x[i]+x[i+1] in x[i+2:] for i in range(len(x)) if i + 2 < len(x)])

print(len(list(filter(
    filter1,
    filter(
        filter2,
        open("day5.txt", "r").readlines())))))