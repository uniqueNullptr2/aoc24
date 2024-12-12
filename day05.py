from math import ceil
def parse(path):
    with open(path, 'r') as f:
        parts = f.read().split("\n\n")
        rules = {}
        updates = []
        for line in parts[0].splitlines():
            t = [int(x) for x in line.strip().split("|")]
            if not t[0] in rules:
                rules[t[0]] = [t[1]]
            else:
                rules[t[0]].append(t[1])
        for line in parts[1].splitlines():
            updates.append([int(x) for x in line.strip().split(",")])
    return (rules,updates)

def check_update(update, rules):
    for i,n in enumerate(update):
        if n in rules:
            for x in rules[n]:
                if x in update[:i]:
                    return (i,update[:i].index(x), 0)
    else:
        return (0, 0, update[ceil(len(update)/2)-1])
def part_a(data):
    rules, updates = data
    s = 0
    for update in updates:
        _,_,x = check_update(update, rules)
        s += x 
    return s
def part_b(data):
    rules, updates = data
    s = 0
    for update in updates:
        _, _, x = check_update(update, rules)
        if x == 0:
            while True:
                i, e, x = check_update(update, rules)
                if x != 0:
                    s += x
                    break
                update[i], update[e] = update[e], update[i]
    return s

def run(path):
    data= parse(path)
    resa = part_a(data)
    resb = part_b(data)
    return (resa,resb)