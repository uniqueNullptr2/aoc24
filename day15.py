import pprint
def parse(path):
    m = []
    instructions = []
    with open(path, 'r') as f:
        x,y = (0,0)
        parts = f.read().strip().split("\n\n")
        for i,line in enumerate(parts[0].splitlines()):
            tmp = []
            for e,ch in enumerate(line.strip()):
                tmp.append(ch)
                if ch == "@":
                    x,y = (e,i)
            m.append(tmp)
        for line in parts[1]:
            for ch in line.strip():
                instructions.append(ch)
    return (x,y,m,instructions)

def part_a(data):
    sx,sy,m,inst = data

    return 0
def part_b(data):
    return 0

def run(path):
    data= parse(path)
    resa = part_a(data)
    resb = part_b(data)
    return (resa,resb)