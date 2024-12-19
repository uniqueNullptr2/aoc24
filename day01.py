
def parse(text):
    lista = []
    listb = []
    for line in text.strip().splitlines():
        p = line.strip().split()
        lista.append(int(p[0]))
        listb.append(int(p[1]))
    return (lista,listb)

def part_a(lista, listb):
    lista = lista[::]
    listb = listb[::]
    lista.sort()
    listb.sort()
    return sum([abs(a-b) for a,b in zip(lista, listb)])
def part_b(lista, listb):
    m = {}
    for x in listb:
        if x in m:
            m[x] += 1
        else:
            m[x] = 1
    s = 0
    for x in lista:
        if x in m:
            s += x * m[x]
    return s

def run(path):
    lista, listb = parse(path)
    resa = part_a(lista, listb)
    resb = part_b(lista, listb)
    return (resa,resb)