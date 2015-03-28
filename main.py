#!/usr/bin/env python
import sys

import cpu
import memory
import programloader
import console


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage:'
        print './main.py <program>'
        sys.exit(1)

    cpu = cpu.CPU()
    memory = memory.Memory()
    console = console.Console()
    
    cpu.memory = memory
    cpu.console = console
    
    loader = programloader.ProgramLoader(memory)
    loader.load_file(sys.argv[1])
    
    cpu.run(0xC000)
