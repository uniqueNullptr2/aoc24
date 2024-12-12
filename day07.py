from tqdm import tqdm
def parse(path):
    ret = []
    with open(path, 'r') as f:
        for line in f.readlines():
            parts = line.split(":")
            parts1 = parts[1].strip().split()
            ret.append((int(parts[0]), [int(x) for x in parts1]))
    return ret

def evaluate(operands, operators,res, acc = None, pos = 1):
    if acc is None:
        acc = operands[0]
    for op in operators:
        if op == "+":
            r =  acc + operands[pos]
        elif op == "*":
            r =  acc * operands[pos]
        elif op == "|":
            r =  int(str(acc) + str(operands[pos]))

        if acc > res:
            return False
        elif pos == len(operands) - 1:
            if res == r:
                return True
        elif evaluate(operands, operators, res, acc=r, pos=pos+1):
            return True
    return False

def part_a(data):
    c = 0
    for res, ops in tqdm(data):
        if evaluate(ops, ["+", "*"], res):
            c += res
    return c
def part_b(data):
    c = 0
    for res, ops in tqdm(data):
        if evaluate(ops, ["+", "*", "|"], res):
            c += res
    return c

def run(path):
    data= parse(path)
    resa = part_a(data)
    resb = part_b(data)
    return (resa,resb)