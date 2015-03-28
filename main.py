#!/usr/bin/env python
import sys

from cpu import CPU
from memory import Memory
from console import Console
from programloader import ProgramLoader


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage:'
        print './main.py <program>'
        sys.exit(1)

    memory = Memory()
    console = Console()

    cpu = CPU(memory, console)
    
    loader = ProgramLoader(memory)
    loader.load_file(sys.argv[1])
    
    cpu.run(0xC000)
