def parse(path):
    ret = []
    with open(path, 'r') as f:
        for line in f.readlines():
            ret.append([ch for ch in line.strip()])

    return ret

def flood_plots(data):
    ret = []

    s = set()
    for i, l in enumerate(data):
        for e,n in enumerate(l):
            if not (e,i) in s:
                stack = [(e,i)]
                plot = n
                area = 0
                fences = 0
                side_cache = set()

                while len(stack) > 0:
                    x,y = stack.pop()
                    if (x,y) in s:
                        continue
                    area += 1
                    s.add((x,y))
                    for xx,yy,v in [(x-1,y,"L"), (x+1,y,"R"), (x,y+1,"D"), (x,y-1,"U")]:
                        if 0 <= xx < len(data[0]) and 0 <= yy < len(data) and data[yy][xx] == plot:
                            if not (xx,yy) in s:
                                stack.append((xx,yy))
                        else:
                            fences += 1
                            side_cache.add((x,y,v))
                
                sides = 0
                ss = set()
                for x,y,v in side_cache:
                    n = data[y][x]
                    if not (x,y,v) in ss:
                        sides += 1
                        stack = [(x,y,v)]
                        while len(stack) > 0:
                            x,y,v = stack.pop()
                            if (x,y,v) in ss or data[y][x] != n:
                                continue
                            ss.add((x,y,v))
                            for xx,yy in [(x,y+1), (x,y-1), (x+1,y), (x-1,y)]:
                                if 0 <= xx < len(data[0]) and 0 <= yy < len(data):
                                    if v == "L" and (x-1 < 0 or data[y][x-1] != n):
                                        stack.append((xx,yy,v))
                                    elif v == "R" and (x+1 >= len(data[0]) or data[y][x+1] != n):
                                        stack.append((xx,yy,v))
                                    elif v == "U" and (y-1 < 0 or data[y-1][x] != n):
                                        stack.append((xx,yy,v))
                                    elif v == "D" and (y+1 >= len(data) or data[y+1][x] != n):
                                        stack.append((xx,yy,v))


                print(f"{plot}: a={area}, f={fences}, s={sides}")
                ret.append((area,fences,sides))
    return ret                
def part_a(data):

    return sum([a*f for a,f,_ in flood_plots(data)])
def part_b(data):
    return sum([a*s for a,_,s in flood_plots(data)])

def run(path):
    data= parse(path)
    price_a = 0
    price_b = 0
    for area, fences, sides in flood_plots(data):
        price_a += area*fences
        price_b += area * sides
    return (price_a, price_b)