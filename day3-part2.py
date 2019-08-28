inp = open("day3.txt", 'r').read()

def move(moves):
    s = set()
    s.add((0,0))
    x = 0
    y = 0
    for n in moves:
        if n == ">":
            x += 1
            s.add((x,y))
        elif n == "<":
            x -= 1
            s.add((x,y))
        elif n == "v":
            y += 1
            s.add((x,y))
        elif n == "^":
            y -= 1
            s.add((x,y))
    return s

print(len(move(inp[::2]).union(move(inp[1::2]))))