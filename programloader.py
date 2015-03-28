import struct


class ProgramLoader(object):
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
