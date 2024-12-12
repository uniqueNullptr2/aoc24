def parse(path):
    x = None
    y = None
    with open(path, 'r') as f:
        map = []
        for i,line in enumerate(f.readlines()):
            tmp = []
            for e,ch in enumerate(line.strip()):
                if ch == "^":
                    x = e
                    y = i
                tmp.append(ch)
            map.append(tmp)
    return (x,y,map)

def rotate(x, y):
    if (x,y) == (0,-1):
        return (1,0)
    elif (x,y) == (1,0):
        return (0,1)
    elif (x,y) == (0,1):
        return (-1,0)
    else:
        return (0,-1)

def find_path(x,y,dx,dy,map):
    c = set()
    s = set()
    c.add((x,y))
    s.add((x,y,dx,dy))
    while True:
        xx = x + dx
        yy = y + dy
        if xx < 0 or yy < 0 or xx >= len(map[0]) or yy >= len(map):
            return (c,s,False)
        if (xx,yy,dx,dy) in s:
            return (c,s,True)
        if map[yy][xx] == "#":
            dx,dy = rotate(dx,dy)
        else:
            x = xx
            y = yy
            c.add((x,y))
        s.add((x,y,dx,dy))

def part_a(data):
    x,y,map = data
    c,_,_ = find_path(x,y,0,-1,map)
    return len(c)

def part_b(data):
    x,y,map = data
    c = set()
    dx = 0
    dy = -1
    cc = 0
    while True:
        xx = x + dx
        yy = y + dy
        if xx < 0 or yy < 0 or xx >= len(map[0]) or yy >= len(map):
            break
        if (xx,yy) not in c and map[yy][xx] !="#":
            map[yy][xx] = "#"
            _,ss,loop = find_path(x,y,dx,dy,map)
            map[yy][xx] = "."
            if loop:
                cc += 1
        if map[yy][xx] == "#":
            dx,dy = rotate(dx,dy)
        else:
            x = xx
            y = yy
            c.add((x,y))
    return cc

def run(path):
    data= parse(path)
    resa = part_a(data)
    resb = part_b(data)
    return (resa,resb)