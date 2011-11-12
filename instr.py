from instruction_set import instruction_set


for id, instr in instruction_set.items():
    instr = instr[0].split(" ")
    line = "instruction_set[" + hex(id) + "] = ('"
    line += instr[0] + "','" + instr[1] + "')"
    
    if instr[0] != '???':
        print line
        
        
for id, instr in instruction_set.items():
    instr = instr[0].split(" ")
    line = "instruction_set[" + hex(id) + "] = ('"
    line += instr[0] + "','" + instr[1] + "')"
    
    if instr[0] == '???':
        print line