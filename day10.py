def parse(path):
    ret = []
    with open(path, 'r') as f:
        for line in f.readlines():
            tmp = []
            for ch in line.strip():
                if ch == ".":
                    tmp.append(-1)
                else:
                    tmp.append(int(ch))
            ret.append(tmp)
    return ret


def find_trailheads(x,y,data,trail=[], last = None):
    if last == 8 and data[y][x] == 9:
        
        return [trail[::]+[(x,y)]]
    elif last is None and data[y][x] == 0 or data[y][x] - last == 1:
        ret = []
        trail.append((x,y))
        if x -1 >= 0:
            ret += find_trailheads(x-1,y,data,trail,data[y][x])
        if x +1 < len(data[0]):
            ret += find_trailheads(x+1,y,data,trail,data[y][x])
        if y -1 >= 0:
            ret += find_trailheads(x,y-1,data,trail,data[y][x])
        if y+1 < len(data):
            ret += find_trailheads(x,y+1,data,trail,data[y][x])
        trail.pop()
        return ret

    else:
        return []


def part_a(data):
    s = 0
    for i,l in enumerate(data):
        for e, n in enumerate(l):
            if n == 0:
                t = find_trailheads(e,i,data)
                tt = set([l[-1] for l in t])
                s += len(tt)
    return s
def part_b(data):
    s = 0
    for i,l in enumerate(data):
        for e, n in enumerate(l):
            if n == 0:
                t = find_trailheads(e,i,data)
                # tt = set([l[-1] for l in t])
                s += len(t)
    return s

def run(path):
    data= parse(path)
    resa = part_a(data)
    resb = part_b(data)
    return (resa,resb)