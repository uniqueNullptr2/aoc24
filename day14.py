from util import matrix_print
from math import floor


class Robot:
    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.init_x = x
        self.init_y = y
    def move(self, w,h):
        self.x += self.vx
        self.y += self.vy
        if self.x >= w:
            self.x -= w
        elif self.x < 0:
            self.x += w
        if self.y >= h:
            self.y -= h
        elif self.y < 0:
            self.y += h
    def reset(self):
        self.x = self.init_x
        self.y = self.init_y
    def __str__(self):
        return f"[Robot x='{self.x}' y='{self.y}' vx='{self.vx}' vy='{self.vy}']"

def parse(txt):
    ret = []
    for line in txt.strip().splitlines():
        parts = line.strip().split()
        pp = parts[0][2:].strip().split(",")
        pv = parts[1][2:].strip().split(",")
        ret.append(Robot(int(pp[0]), int(pp[1]), int(pv[0]), int(pv[1])))
    return ret


def check_tree(tree,width):
    for l in tree:
        c = 0
        for x in l:
            if x > 0:
                c += 1
            else:
                c = 0
            if c > width/4:
                return True
    return False


def count(robots,w,h):
    hh = floor(h / 2)
    hw = floor(w / 2)
    c1 = len([r for r in robots if r.x < hw and r.y < hh])
    c2 = len([r for r in robots if r.x > hw and r.y < hh])
    c3 = len([r for r in robots if r.x < hw and r.y > hh])
    c4 = len([r for r in robots if r.x > hw and r.y > hh])
    return c1*c2*c3*c4


def part_a(data, width, height):
    for _ in range(100):
        for r in data:
            r.move(width, height)

    return count(data, width,height)


def part_b(data,width,height):
    b = []
    for _ in range(height):
        t = []
        for _ in range(width):
            t.append(0)
        b.append(t)
    for r in data:
        b[r.y][r.x] += 1

    i = 0
    while True:
        if check_tree(b,width):
            # matrix_print(b)
            return i
        for r in data:
            b[r.y][r.x] -= 1
            r.move(width, height)
            b[r.y][r.x] += 1
        i += 1


def run(path,width=101,height=103):
    data= parse(path)
    resa = part_a(data,width,height)
    for r in data:
        r.reset()
    resb = part_b(data,width,height)
    return (resa,resb)