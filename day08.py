def parse(path):
    ret = {}
    with open(path, 'r') as f:
        lines = f.readlines()
        width = len(lines[0].strip())
        height = len(lines)
        for i,line in enumerate(lines):
            for e,ch in enumerate(line.strip()):
                if ch != ".":
                    if ch in ret:
                        ret[ch].append((e,i))
                    else:
                        ret[ch] = [(e,i)]

    return (width,height,ret)

def part_a(data):
    w,h,frequencies = data
    s = set()
    for freq in frequencies:
        ant = frequencies[freq]
        for i in range(0,len(ant)-1):
            for e in range(i+1, len(ant)):
                x1,y1 = ant[i]
                x2,y2 = ant[e]
                dx = x2 - x1
                dy = y2 - y1

                x3 = x1 - dx
                y3 = y1 - dy

                x4 = x2 + dx
                y4 = y2 + dy

                if x3 >= 0 and x3 < w and y3 >= 0 and y3 < h:
                    s.add((x3,y3))
                if x4 >= 0 and x4 < w and y4 >= 0 and y4 < h:
                    s.add((x4,y4))
    # for x,y in s:
    #     print(f"{y}/{x}")
    return len(s)

def points(x,y,dx,dy,w,h):
    ret = []
    while 0 <= x < w and 0 <= y < h:
        ret.append((x,y))
        x += dx
        y += dy
    return ret
def part_b(data):
    w,h,frequencies = data
    s = set()
    for freq in frequencies:
        ant = frequencies[freq]
        for i in range(0,len(ant)-1):
            for e in range(i+1, len(ant)):
                x1,y1 = ant[i]
                x2,y2 = ant[e]
                dx = x2 - x1
                dy = y2 - y1

                # x3 = x1 - dx
                # y3 = y1 - dy

                # x4 = x2 + dx
                # y4 = y2 + dy

                for x,y in points(x1,y1,-dx,-dy,w,h) + points(x2,y2,dx,dy,w,h):
                    s.add((x,y))
    # for x,y in s:
    #     print(f"{y}/{x}")
    return len(s)

def run(path):
    data= parse(path)
    resa = part_a(data)
    resb = part_b(data)
    return (resa,resb)