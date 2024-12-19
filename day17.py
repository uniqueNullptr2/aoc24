def parse(txt):
    lines = txt.strip().splitlines()
    a = int(lines[0].strip().split(": ")[1])
    b = int(lines[1].strip().split(": ")[1])
    c = int(lines[2].strip().split(": ")[1])
    mem = [int(x) for x in lines[4].strip().split(": ")[1].split(",")]
    return a,b,c,mem


class CPU:
    def __init__(self, a,b,c,mem):
        self.mem = mem
        self.a = a
        self.b = b
        self.c = c
        self.ip = 0
        self.out = []
    def cpu_set(self,a, b,c):
        self.a = a
        self.b = b
        self.c = c
        self.ip = 0
        self.out = []
    def combo(self):
        return [0,1,2,3,self.a, self.b, self.c][self.lit()]
    def lit(self):
        return self.mem[self.ip+1]
    def step(self, out=False):
        if self.ip+1 >= len(self.mem):
            return 1
        op = self.mem[self.ip]
        if op == 0: # adv
            self.a = self.a // (2**self.combo())
            self.ip += 2
        elif op == 1:
            self.b ^= self.lit()
            self.ip += 2
        elif op == 2:
            self.b = self.combo()%8
            self.ip += 2
        elif op == 3:
            if self.a != 0:
                self.ip = self.lit()
            else:
                self.ip += 2
        elif op == 4:
            self.b ^= self.c
            self.ip += 2
        elif op == 5:
            self.out.append(self.combo()%8)
            # print(f"{out} and {self.out[-1]} != {self.mem[len(self.out)-1]} => {out and self.out[-1] != self.mem[len(self.out)-1]}")
            if out and self.out[-1] != self.mem[len(self.out)-1]:
                return -1
            self.ip += 2
        elif op == 6:
            self.b = self.a // (2**self.combo())
            self.ip += 2
        elif op == 7:
            self.c = self.a // (2**self.combo())
            self.ip += 2
        return 0
    def run(self, out=False,debug=False):
        while True:
            b = self.step(out)
            if debug:
                self.pstate()
            if not b == 0:
                return b
    def pstate(self):
        print(f"a: {self.a}, b: {self.b}, c: {self.c}, ip: {self.ip}")
    def output(self):
        return ",".join([str(x) for x in self.out])


# def reverse_cpu()
def part_a(data):
    a,b,c,mem = data
    cpu = CPU(a,b,c,mem)
    cpu.run()
    return cpu.output()
def part_b(data):
    i = 0
    _,b,c,mem = data
    cpu = CPU(i,b,c,mem)
    while True:
        if i % 100000==0:
            print(i)
        cpu.cpu_set(i,b,c)
        b = cpu.run(True)

        # print(b)
        # print(cpu.out)
        if b == 1 and cpu.out == mem:
            return i
        i += 1

def run(path,a=True,b=True):
    data= parse(path)
    resa = part_a(data) if a else None
    resb = part_b(data) if b else None
    return (resa,resb)