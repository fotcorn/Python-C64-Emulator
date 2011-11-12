import cpu
import memory
import programloader

if __name__ == "__main__":
    cpu = cpu.CPU()
    memory = memory.Memory()
    cpu.memory = memory
    
    loader = programloader.ProgramLoader(memory)
    loader.load_file('/home/corn/Projekte/6502emu/examples/asm/count10')
    
    cpu.run(0xC000)
