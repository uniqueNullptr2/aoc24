import re
def parse(text):
    return text

def compute_mul(mul):
    p1 = mul.split('(')
    p2 = p1[1].split(',')
    return int(p2[0]) * int(p2[1][:-1])

def part_a(data):
    m = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
    return sum([compute_mul(mm) for mm in m])

def part_b(data):
    m = re.findall(r"do\(\)|don't\(\)|mul\(-?\d{1,3},-?\d{1,3}\)", data)
    s = 0
    enabled = True
    for inst in m:
        if inst == "do()":
            enabled = True
        elif inst == "don't()":
            enabled = False
        elif inst.startswith("mul(") and enabled:
            s += compute_mul(inst)
    return s

def run(path):
    data= parse(path)
    resa = part_a(data)
    resb = part_b(data)
    return (resa,resb)