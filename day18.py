from util import matrix_print as mprint
from heapq import heapify, heappush, heappop
def parse(text):
    ret = []
    for line in text.strip().splitlines():
        p = line.strip().split(",")
        ret.append((int(p[0]), int(p[1])))
    return ret

def create_map(data,d):
    m = [["." for _ in range(d)] for _ in range(d)]
    return m

class Item:
    def __init__(self,x,y,p,d):
        self.x = x
        self.y = y
        self.p = p
        self.d = d
    def __lt__(self, other):
        return self.p < other.p
    def step(self):
        return [Item(self.x+dx,self.y+dy,self.p+1,self.d) for dx,dy in [(1,0), (-1,0),(0,1),(0,-1)]if 0 <= self.x+dx < self.d and 0 <= self.y + dy < self.d]
    def xy(self):
        return self.x,self.y

def dijkstraaaa(m,d,debug=False):
    win = None
    heap = []
    heapify(heap)
    heappush(heap,Item(0,0,0,d))
    s = set()
    while len(heap) > 0:
        item = heappop(heap)
        m[item.y][item.x] = item.p
        if item.xy() in s:
            continue
        s.add(item.xy())

        if not win is None:
            if debug:
                mprint(m)
            return win
        if item.xy() == (d-1,d-1) and (win is None or item.p < win):
            win = item.p
        for i in item.step():
            if not i.xy() in s and not m[i.y][i.x] == "X":
                heappush(heap,i)
    if debug:
        mprint(m)
    return win

def check_path(m):
    stack = [(len(m)-1,len(m)-1)]
    s = set()
    while len(stack) > 0:
        x,y = stack.pop()
        if (x,y) in s:
            continue
        s.add((x,y))
        if (x,y) == (0,0):
            return True
        for dx,dy in [(1,0), (-1,0),(0,1),(0,-1)]:
            xx = x+dx
            yy = y+dy
            if 0 <= xx < len(m) and 0 <= yy < len(m) and m[yy][xx] != "X":
                stack.append((xx,yy))
    return False


def run(path,a=True,b=True,d=71,c=1024):
    data= parse(path)
    m = create_map(data,d)
    for x,y in data[:c]:
        m[y][x] = 'X'
    resa = dijkstraaaa(m,d)
    # mprint(m)
    resb = None
    for x,y in data[c:]:
        m[y][x] = "X"
        if not check_path(m):
            resb = f"{x},{y}"
            break
    return (resa,resb)