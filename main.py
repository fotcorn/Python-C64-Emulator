import cpu
import memory
import programloader
import console

if __name__ == "__main__":
    cpu = cpu.CPU()
    memory = memory.Memory()
    console = console.Console()
    
    cpu.memory = memory
    cpu.console = console
    
    loader = programloader.ProgramLoader(memory)
    loader.load_file('/home/corn/Projekte/6502emu/examples/conditional_jumps/task1')
    
    cpu.run(0xC000)
