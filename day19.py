def parse(text):
    lines = text.strip().splitlines()
    towels = lines[0].strip().split(", ")
    patterns = [line.strip() for line in lines[2:]]

    return towels, patterns

def find(l,s, mem={}):
    c = 0 
    if s in mem:
        return mem[s]
    for ll in l:
        if s == ll:
            c += 1
        elif s.startswith(ll):
           c += find(l, s[len(ll):], mem)
    mem[s] = c
    return c

def run(path,a=True,b=True):
    towels,patterns = parse(path)
    resa = 0
    resb = 0
    for p in patterns:
        t = find(towels, p)
        if t > 0:
            resa += 1
        resb += t
    return (resa,resb)