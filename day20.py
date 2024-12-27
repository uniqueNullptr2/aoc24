from heapq import heapify, heappush, heappop
from util import matrix_print as mprint
def parse(text):
    ret = []
    sx = 0
    sy = 0
    for i,line in enumerate(text.strip().splitlines()):
        tmp = []
        for e,ch in enumerate(line.strip()):
            tmp.append(ch)
            if ch == "S":
                sx = e
                sy = i
        ret.append(tmp)
    return sx,sy,ret

class Item:
    def __init__(self,x,y,p):
        self.x = x
        self.y = y
        self.p = p
    
    def moves(self,m):
        ret = []
        for dx,dy in [(1,0), (-1,0), (0,-1), (0,1)]:
            xx = self.x + dx
            yy = self.y + dy
            if 0 <= xx < len(m[0]) and 0 <= yy < len(m):
                ch = m[yy][xx]
                if ch == "." or ch == "E":
                    ret.append(Item(xx,yy,self.p+1))
                # elif self.ch < 1 or self.is_ob and self.ob < 2:
                #     ret.append(Item(xx,yy,1,self.ob + 1,True, self.p+1))
        return ret
    def __lt__(self,o):
        return self.p < o.p

    def xy(self):
        return (self.x,self.y)

def dijkstra(sx,sy,m):
    ret = []
    heap = []
    heapify(heap)
    heappush(heap,Item(sx,sy,0))
    m[sy][sx] = 0
    s = set()
    while len(heap) > 0:

        item = heappop(heap)
        # s.add(item.xy())
        for i in item.moves(m):
            if m[i.y][i.x] == "E":
                m[i.y][i.x] = i.p
                return i.x,i.y,i.p
            # s.add(i.xy())
            m[i.y][i.x] = i.p
            heappush(heap,i)
    return -1

def check_cheat2(x,y,m,s,p,d=0):
    r = None
    for dx,dy in [(1,0), (-1,0), (0,-1), (0,1)]:
        xx = x + dx
        yy = y + dy
        if 0 <= xx < len(m[0]) and 0 <= yy < len(m):
            if isinstance(m[yy][xx], int) and m[yy][xx] < p:
                t = p-m[yy][xx] - d
                if r is None or t > r:
                    r = t
            elif d < 2:
                s.add((xx,yy))
                t = check_cheat(xx,yy,m,s,p,d+1)
                if not t is None and (r is None or t > r) :
                    r = t
    
    return r
def check_cheat(x,y,m,p):
    r = []
    for dx,dy in [(1,0), (-1,0), (0,-1), (0,1)]:
        xx = x + dx*2
        yy = y + dy*2
        if 0 <= xx < len(m[0]) and 0 <= yy < len(m):
            if isinstance(m[yy][xx], int) and m[yy][xx] < p:
                t = p-m[yy][xx]
                r.append(t-2)
                
    
    return r
def check_path(ex,ey,p,m, ev):
    c = 0
    x,y = ex,ey
    while m[y][x] != 0:
        t = check_cheat(x,y,m,p)
        tx,ty = x,y
        for tt in t:
            if tt >= ev:
                c += 1
        for dx,dy in [(1,0), (-1,0), (0,-1), (0,1)]:
            xx = x + dx
            yy = y + dy
            if isinstance(m[yy][xx],int) and p - m[yy][xx] == 1 or m[yy][xx] == "S":
                tx=xx
                ty=yy
                p = m[yy][xx]
        x,y = tx,ty

    return c
def part_a(data, ev):
    sx,sy,m = data
    ex,ey,p = dijkstra(sx,sy,m)
    t = check_path(ex,ey,p,m,ev)
    return t
def part_b(data):
    return 0

def run(path,a=True,b=True, ev=100):
    data= parse(path)
    resa = part_a(data,ev) if a else None
    resb = part_b(data) if b else None
    return (resa,resb)