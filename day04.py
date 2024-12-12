def parse(path):
    ret = []
    with open(path, 'r') as f:
        for line in f.readlines():
            ret.append(line.strip())
    return ret

def filter(x, y, width, height):
    points = [(x+1,y),(x-1,y), (x+1,y+1), (x+1,y-1), (x-1, y+1), (x-1, y-1), (x,y+1), (x,y-1)]
    return [(x,y) for x,y in points if x >+ 0 and y >= 0 and y < height and x < width]

def find_all(char, data):
    ret = []
    for i,l in enumerate(data):
        for e,c in enumerate(l):
            if c == char:
                ret.append((e,i))
    return ret

def part_a(data):
    c = 0
    for x,y in find_all('X', data):
        for dx, dy in [(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1)]:
            for i, ch in enumerate("XMAS"):
                xx = x + i*dx
                yy = y + i*dy
                if xx >=0 and yy >= 0 and xx < len(data[0]) and yy < len(data) and data[yy][xx] == ch:
                    pass
                else:
                    break
            else:
                c += 1
    return c
def part_b(data):
    c = 0
    word = "XMAS"
    for x,y in find_all('A', data):
        if x > 0 and y > 0 and x < len(data[0]) -1 and y < len(data) - 1:
            b1 = data[y-1][x-1] == 'M' and data[y+1][x+1]=='S' or data[y-1][x-1] == 'S' and data[y+1][x+1]=='M'
            b2 = data[y-1][x+1] == 'M' and data[y+1][x-1]=='S' or data[y-1][x+1] == 'S' and data[y+1][x-1]=='M'
            c += b1 and b2
    return c

def run(path):
    data= parse(path)
    resa = part_a(data)
    resb = part_b(data)
    return (resa,resb)