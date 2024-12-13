def parse(path):
    ret = None
    with open(path, 'r') as f:
        ret = [int(x) for x in f.read().strip().split()]
    return ret

def process(data, n):
    mem = {}
    return sum([process_rec(x,n,mem) for x in data])

def process_rec(x, n, mem):
    t = x
    y = None
    xx = str(x)
    zero = x == 0

    if (x,n) in mem:
        return mem[(x,n)]

    if x == 0:
        x = 1
    elif len(xx) %2 == 0:
        f = len(xx)//2
        x = int(xx[:f])
        y = int(xx[f:])
    else:
        x *= 2024
    n -= 1
    if n == 0:
        if not y is None:
            return 2
        else:
            return 1
    else:
        if not y is None:
            s = process_rec(y,n,mem) + process_rec(x,n,mem)
        else:
            s = process_rec(x,n,mem)
            mem[(t,n+1)] = s
        return s
def part_a(data):
    return process(data,25)
def part_b(data):
    return process(data,75)

def run(path):
    data= parse(path)
    resa = part_a(data)
    resb = part_b(data)
    return (resa,resb)