def parse(path):
    ret = []
    with open(path, 'r') as f:
        line = f.read().strip()
        flag = True
        i = 0
        for ch in line:
            d = int(ch)
            if flag:
                ret += [i] * d
                i += 1
            else:
                ret += [None]*d
            flag = not flag
    return ret

def part_a(data):
    data = data[::]
    l = 0
    r = len(data) - 1
    # print(data)
    while True:
        while not data[l] is None:
            l += 1
        while data[r] is None:
            r -= 1
        if l >= r:
            break
            
        # print(f"{l} - {r}")
        data[l], data[r] = data[r], data[l]

    # print(data)
    
    return sum([i*e for i,e in enumerate(data) if not e is None])

def get_len(arr, i, rev=False):
    c = arr[i]
    l = 0
    while not rev and i < len(arr) and arr[i] == c:
        l += 1
        i += 1
    while rev and i >= 0 and arr[i] == c:
        l += 1
        i -= 1
    return l

def part_b(data):
    empty = {}
    files = []

    i = 0
    while i < len(data):
        c = data[i]
        l = get_len(data,i)
        if c is None:
            if l in empty:
                empty[l].append(i)
            else:
                empty[l] = [i]
        else:
            files.append((c,i,l))        
        i += l
    
    # print(empty)
    # print(data)
    for id, i, l in files[::-1]:
        x = None
        for ll in empty:
            if (x is None or empty[ll][0] < empty[x][0]) and ll >= l and empty[ll][0] < i:
                x = ll
                
        if not x is None:
            e = empty[x].pop(0)
            for y in range(l):
                data[e+y], data[i+y] = data[i+y], data[e+y]
            d = x - l
            if len(empty[x]) == 0:
                del empty[x]
            if d > 0:
                empty[d].append(e+l)
                empty[d].sort()

    # print(empty)
    # print(data)
    return sum([i*e for i,e in enumerate(data) if not e is None])

def run(path):
    data= parse(path)
    resa = part_a(data)
    resb = part_b(data)
    return (resa,resb)