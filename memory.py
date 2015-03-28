

class Memory(object):

    def __init__(self):
        self.memory = {}  # allocate 65kb memory
    
    def write(self, address, value):
        if address < 0 or address > 2**16:
            raise Exception("Address out of range: " + address)
        if not isinstance(value, int) or value < 0 or value > 255:
            raise Exception("Wrong Value: " + str(value))
        self.memory[address] = value
    
    def read(self, address):
        if address < 0 or address > 2**16:
            raise Exception("Address out of range: " + str(address))
        if not address in self.memory:
            return 0
        
        return self.memory[address]
