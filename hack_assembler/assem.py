#!/usr/bin/python
import sys

from code import Code
from parser import Parser
from symboltable import SymbolTable

"""
First pass:

# build symboltable
rom_address = o
for line in parsed.cmds:
    if parsed.command_type() is "C" or "A":
        symboltable.add(line, rom_address)
        rom_address += 1
    elif parsed.command_type() is "L":
        symboltable.add(line, rom_address + 1)

Second pass:
for line in cmds do
    if line is symbol do
        if symbol in ST
            ST.replace(symbol, numeric value) && complete traslation
        else:
            ST.add(symbol, RAMADDRESS from 16 on)

"""


if __name__ == "__main__":
    code_obj = Code()
    st = SymbolTable()
    input_file = sys.argv[1]
    parsed = Parser(input_file)
    ML = []
    rom_address = 0
    # with open("{0}.hack".format(input_file), "w") as resulting_file:
    while parsed.has_more_cmds():
        if parsed.command_type() == "C_COMMAND" or parsed.command_type() == "A_COMMAND":
            st.add_entry(parsed.cmds[parsed.command_index], rom_address)
            rom_address += 1
        elif parsed.command_type() == "L_COMMAND":
            st.add_entry(parsed.cmds[parsed.command_index], rom_address + 1)
        parsed.advance()
    
    while parsed.has_more_cmds():

    print "ML: ", ML
    for line in ML:
        print "line: ", line
        resulting_file.write(str(line))
