def parse(text):
    ret = None
    for line in text.strip().splitlines():
        pass
    return ret

def part_a(data):
    return 0
def part_b(data):
    return 0

def run(path,a=True,b=True):
    data= parse(path)
    resa = part_a(data) if a else None
    resb = part_b(data) if b else None
    return (resa,resb)