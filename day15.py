import pprint
def parse(path):
    m = []
    instructions = []
    with open(path, 'r') as f:
        x,y = (0,0)
        parts = f.read().strip().split("\n\n")
        for i,line in enumerate(parts[0].splitlines()):
            tmp = []
            for e,ch in enumerate(line.strip()):
                tmp.append(ch)
                if ch == "@":
                    x,y = (e,i)
            m.append(tmp)
        for line in parts[1]:
            for ch in line.strip():
                instructions.append(ch)
    return (x,y,m,instructions)

VECS = {
    ">": (1,0,False),
    "<": (-1,0,False),
    "v": (0,1,True),
    "^": (0,-1,True),
}


def mprint(m):
    s = ""
    for l in m:
        for ch in l:
            s += ch
        s += "\n"
    print(s[:-1])


def move(l, m, inst):
    n = set()

    dx,dy,v = VECS[inst]
    w = len(m[0])
    h = len(m)
    for x,y in l:
        xx = x+dx
        yy = y + dy
        if w <= xx < 0 or h <= yy < 0 or m[yy][xx] == "#":
            return False
        else:
            ch = m[yy][xx]
            if ch != ".":
                n.add((xx,yy))
            if ch == "[" and v:
                n.add((xx+1,yy))
            if ch == "]" and v:
                n.add((xx-1,yy))
    if len(n) == 0 or move(n, m, inst):
        for x,y in l:
            m[y+dy][x+dx],m[y][x] = m[y][x],m[y+dy][x+dx]
        return True
    else:
        return False


def process(x,y,m,inst, debug=False):
    for ins in inst:
        if debug:
            mprint(m)
            print(ins)
            print("\n")
            input()
        b = move([(x,y)],m,ins)
        dx,dy,_ = VECS[ins]
        if b:
            x += dx
            y += dy
    
    

def gps(m):
    s = 0
    for i, l in enumerate(m):
        for e,ch in enumerate(l):
            if ch == "O" or ch == "[":
                s += i*100 + e
    return s

def transform_map(m):
    x = 0
    y = 0
    m2 = []
    for l in m:
        tmp = []
        for ch in l:
            if ch == "#":
                tmp += ["#","#"]
            elif ch == ".":
                tmp += [".","."]
            elif ch == "O":
                tmp += ["[","]"]
            else:
                x = len(tmp)
                y = len(m2)
                tmp += ["@", "."]
        m2.append(tmp)
    return x,y,m2


def run(path):
    data= parse(path)
    x1,y1,m,inst = data
    x2,y2,m2 = transform_map(m)

    process(x1,y1,m,inst)
    resa=gps(m)

    process(x2,y2,m2,inst,False)
    resb =  gps(m2)
    return (resa,resb)