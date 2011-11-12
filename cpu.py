from instruction_set import instruction_set

class StatusRegister():
    def __init__(self):
        self.N = False # negativ
        self.B = False # break
        self.D = False # decimal
        self.I = False # interrupt (IRQ disabled)
        self.Z = False # zero
        self.C = False # carry
    
class Register():
    def __init__(self, size):
        self.size = size
        self.value = 0
        
    def set(self, value):
        if value < 0 or value > 2**self.size:
            raise Exception("Wrong value for register: " + value)
        self.value = value
    
    def get(self):
        return self.value
    
    def inc(self):
        self.set(self.value + 1)
    
    def dec(self):
        self.set(self.value - 1)
        

class CPU():
    def __init__(self):
        self.PC = Register(16) # program counter
        self.A = Register(8) # accumulator
        self.X = Register(8) # x register
        self.Y = Register(8) # y register
        self.SR = StatusRegister() # status register
        self.SP = Register(8) # stack pointer
        
    def run(self, address):
        self.PC.set(address)
        
        
        while True:
            instr = self.fetch()
            if instr[0] == 'BRK impl':
                return
            self.execute(instr)
        
        
    def fetch(self):
        data = self.memory.read(self.PC.get())
        instr = instruction_set[data]
        ret = [instr[0]]
        for i in range(0, instr[1]):
            self.PC.inc()
            ret.append(self.memory.read(self.PC.get()))
        self.PC.inc()
        return ret
    
    def execute(self, instr):
        print instr
    
        
        

        
    