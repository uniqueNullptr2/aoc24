def parse(path):
    ret = []
    with open(path, 'r') as f:
        for line in f.readlines():
            ret.append([int(x) for x in line.strip().split()])
    return ret

def check_level(r0, r1, increase):
    if r0 == r1 or abs(r0 - r1) > 3:
        return False
    elif increase and r0 > r1:
        return False
    elif not increase and r0 < r1:
        return False
    else:
        return True

def check_levels(r, dampeners):
    stack = [(0, 2, 1, r[0] < r[2]), (1, 2,1, r[1] < r[2]), (0, 1, 0, r[0] < r[1])]

    while len(stack) > 0:
        i0, i1, dampened_levels, increase = stack.pop()
        if dampened_levels > dampeners:
            continue
        if check_level(r[i0],r[i1], increase):
            if i1 >= len(r) - (dampeners-dampened_levels) - 1:
                return True
            if i1 < len(r) - 2:
                stack.append((i1, i1+2, dampened_levels+1, increase))
            stack.append((i1, i1+1, dampened_levels, increase))
    return False

def part_a(data):
    c = 0
    for report in data:
        if check_levels(report, 0):
            c += 1
    return c

def build_permutations(report):
    ret = [report]
    for i in range(len(report)):
        tmp = []
        for e,r in enumerate(report):
            if i == e:
                continue 
            tmp.append(r)
        ret.append(tmp)
    return ret

def test(report):
    perms = build_permutations(report)
    for r in perms:
        if check_levels(r,0):
            return True
    return False
def part_b(data):
    c = 0
    for report in data:
        if check_levels(report,1):
            c += 1
    return c

def run(path):
    data= parse(path)
    resa = part_a(data)
    resb = part_b(data)
    return (resa,resb)