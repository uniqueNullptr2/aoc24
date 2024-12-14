import math

def parse(path):
    ret = []
    with open(path, 'r') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            a = lines[i].strip()[12:].split(", Y+")
            b = lines[i+1].strip()[12:].split(", Y+")
            p = lines[i+2].strip()[9:].split(", Y=")
            i += 4
            ret.append((int(a[0]), int(a[1]), int(b[0]), int(b[1]), int(p[0]), int(p[1])))
    return ret

def solv(ax,ay,bx,by,px,py):
    e = (py*ax - px*ay) / (by*ax - bx*ay)
    i = (px - e * bx) / ax
    return i,e

def part_a(data):
    s = 0
    for ax,ay,bx,by,px,py in data:
        a,b = solv(ax,ay,bx,by,px,py)
        if a%1 == 0 and b % 1 == 0 and a <= 100 and b <= 100:
            s += a*3 + b
    return int(s)

def part_b(data):
    s = 0
    for ax,ay,bx,by,px,py in data:
        a,b = solv(ax,ay,bx,by,px+10000000000000,py+10000000000000)
        if a%1 == 0 and b % 1 == 0:
            s += a*3 + b
    return int(s)

def run(path):
    data= parse(path)
    resa = part_a(data)
    resb = part_b(data)
    return (resa,resb)