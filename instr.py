from instruction_set import instruction_set


zero_arg_size = ['A', 'impl']
one_arg_size = ['#', 'ind', 'X,ind', 'ind,Y', 'rel', 'zpg', 'zpg,X', 'zpg,Y']
two_arg_size = ['abs', 'abs,X', 'abs,Y']


for id, instr in instruction_set.items():
    line = "instruction_set[" + hex(id) + "] = ('"
    line += instr[0] + "', '" + instr[1] + "'"
    
    if instr[1] in zero_arg_size:
        size = 0
    if instr[1] in one_arg_size:
        size = 1
    if instr[1] in two_arg_size:
        size = 2
    
    line += ", " + str(size) + ")"
    
    if instr[0] != '???':
        print line
        
        
for id, instr in instruction_set.items():
    line = "instruction_set[" + hex(id) + "] = ('"
    line += instr[0] + "','" + instr[1] + "')"
    
    if instr[0] == '???':
        print line