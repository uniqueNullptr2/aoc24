from heapq import heapify, heappush, heappop
def parse(path):
    ret = []
    sx = 0
    sy = 0
    ex = 0
    ez = 0
    with open(path, 'r') as f:
        for i,line in enumerate(f.readlines()):
            ret.append(line.strip())
            for e,ch in enumerate(line):
                if ch == "S":
                    sx = e
                    sy = i
                elif ch == "E":
                    ex = e
                    ey = i
    return sx,sy, ex, ey,ret

DIRS = ['R', 'D', 'L', 'U']
VECS = {
    'R': (1,0),
    'D': (0,1),
    'L': (-1,0),
    'U': (0,-1),
}

class Position:
    def __init__(self,x,y, d='R', p = 0,):
        self.x = x
        self.y = y
        self.d = d
        self.p = p
    def rotate(self,x, reverse=False):
        i = DIRS.index(self.d)
        i += x
        if reverse:
            p = self.p - 1000
        else:
            p = self.p + 1000
        while i >= len(DIRS):
            i -= len(DIRS)
        while i < 0:
            i += len(DIRS)
        return Position(self.x,self.y,DIRS[i],p)

    def move(self,m, reverse = False):
        w = len(m[0])
        h = len(m)
        x = self.x
        y = self.y
        dx,dy = VECS[self.d]
        if reverse:
            p = self.p - 1
        else:
            p = self.p + 1
        if reverse:
            dx *= -1
            dy *= -1
        if 0 <= x+dx < w and 0 <= y+dy < h and m[y+dy][x+dx] != '#':
            return Position(x+dx,y+dy,self.d,p)
        return None

    def s(self):
        return(self.x, self.y, self.d, self.p)
    def xy(self):
        return (self.x, self.y)

    def __lt__(self, other):
         return self.p < other.p

def dijkstra(sx,sy,m):
    mem = set()
    mem2 = set()
    win = None
    p = Position(sx,sy)
    heap = []
    heapify(heap)
    heappush(heap,p)
    while len(heap) > 0:
        pos = heappop(heap)
        mem.add(pos.s())
        mem2.add((pos.x,pos.y,pos.d))
        if not win is None and pos.p > win:
            return mem,win

        if m[pos.y][pos.x] == 'E':
            win = pos.p

        npos = pos.move(m)
        if not npos is None and not (npos.x,npos.y,npos.d) in mem2:
            heappush(heap, npos)
        for f in [1,-1]:
            npos = pos.rotate(f)
            if not  (npos.x,npos.y,npos.d) in mem2:
                heappush(heap,npos)
    return (mem,None)

def on_path(x,y,mem,m,win):
    b = [Position(x,y,'U',win),Position(x,y,'D',win),Position(x,y,'L',win),Position(x,y,'R',win)]
    mem2 = set()
    s = set()
    tmp = []
    while len(b) > 0:
        for p in b:
            if p.s() in mem:
                # print("br")
                # mem2.add(p.get_pos())
                s.add(p.xy())
                np = p.move(m, True)
                if not np is None:
                    tmp.append(np)
                for f in [-1,1]:
                    np = p.rotate(f,True)
                    tmp.append(np)
        b = tmp
        tmp = []
    return len(s)
def run(path):
    sx,sy,ex,ey,m = parse(path)
    mem, win = dijkstra(sx,sy,m)
    resa = win
    # for x,y,d,p in mem:
        # print(f"{x} - {y} = {d}, {p}")
    # s = set()
    # for ss in paths:
    #     s = s.union(ss)
    # s = find_path(Position(sx,y), m, [(x,y,'R')],win)
    resb = on_path(ex,ey,mem,m,win)
    return (resa,resb)