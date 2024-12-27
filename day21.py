def parse(text):
    return [line.strip() for line in text.strip().splitlines()]

NUMPAD = {
    "A": {"<": "0", "^": "3"},
    "0": {"^": "2", ">": "A"},
    "1": {"^": "4", ">": "2"},
    "2": {"^": "5", ">": "3", "v": "0", "<": "1"},
    "3": {"^": "6", "v": "A", "<": "2"},
    "4": {"^": "7", ">": "5", "v": "1"},
    "5": {"^": "8", ">": "6", "v": "2", "<": "4"},
    "6": {"^": "9", "v": "3", "<": "5"},
    "7": {">": "8", "v": "4"},
    "8": {">": "9", "v": "5", "<": "7"},
    "9": {"v": "6", "<": "8"},
}

DIRPAD = {
    "A": {"v": ">", "<": "^"},
    "^": {">": "A", "v": "v"},
    "<": {">": "v"},
    "v": {"^": "^", ">": ">", "<": "<"},
    ">": {"^": "A", "<": "v"},
}

def parsenum(s):
    t = ""
    for ch in s:
        if ch.isdigit():
            t += ch
    return int(t)
def findpath(start, goal, pad, cache, f=None, debug=False):
    if f is None:
        f = set()
    if debug:
        print(f"{start} => {goal}, set={len(f)}")
    if (start,goal) in cache:
        if debug:
            print(f"debug cache: {cache[(start,goal)]}")
        return cache[(start,goal)]
    if start in f:
        if debug:
            print(f"filter debug: {start}")
        return None
    f.add(start)
    s = None
    r = []
    for t in pad[start]:
        if pad[start][t] == goal:
            return [t]
        else:   
            tmp = findpath(pad[start][t], goal,pad,cache,f,debug)
            if debug:
                print(f"debug loop: {start}+{t} -> {pad[start][t]} = {tmp}")
            if not tmp is None 
                for ttmp in tmp:
                    if s is None or len(ttmp)+1 < s:
                        s = len(ttmp)+1
                        r.append(t+ttmp)
    if not s is None:
        cache[(start,goal)] = r
    return r

def get_code(codes,pad, cache):
    ret = []
    t = "A"
    for code in codes:
        r = []
        for ch in code:
            tmp = findpath(t, ch, pad,cache)
            # print(f"{t} -> {ch}: '{tmp}'")
            r.append(tmp)
            t = ch
    return r
def part_a(data):
    numcache = {}
    dircache = {}
    c = 0
    for s in data:
        n = parsenum(s)
        print(f"{len(s)} -> {s}")

        s = "A".join(get_code(s, NUMPAD, numcache)) + "A"
        print(f"{len(s)} -> {s}")

        s = "A".join(get_code(s, DIRPAD, numcache)) + "A"
        print(f"{len(s)} -> {s}")

        s = "A".join(get_code(s, DIRPAD, numcache))
        print(f"{len(s)} -> {s}")
    
        break
        c+= len(s) * n
    return c
def part_b(data):
    return 0

def run(path,a=True,b=True):
    data= parse(path)
    resa = part_a(data) if a else None
    resb = part_b(data) if b else None
    return (resa,resb)