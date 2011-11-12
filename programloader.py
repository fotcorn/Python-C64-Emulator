import struct
import memory


class ProgramLoader():
    def __init__(self, memory):
        self.memory = memory
    
    def load_file(self, path):
        f = open(path, "r")
        data = f.read()
        f.close()
        
        address = struct.unpack('H', data[:2])[0]
        
        for byte in data[2:]:
            self.memory.write(address, struct.unpack('B', byte)[0])
            address += 1
        
    
if __name__ == '__main__':
    mem = memory.Memory()
    loader = ProgramLoader(mem)
    loader.load_file('/home/corn/Projekte/6502emu/examples/asm/count10')
    
    print mem.memory