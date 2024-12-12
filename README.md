## Snippet for new Day

```python
def parse(path):
    ret = None
    with open(path, 'r') as f:
        for line in f.readlines():
            pass
    return ret

def part_a(data):
    return 0
def part_b(data):
    return 0

def run(path):
    data= parse(path)
    resa = part_a(data)
    resb = part_b(data)
    return (resa,resb)
```