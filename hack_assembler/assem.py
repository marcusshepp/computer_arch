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
    ram_address = 16
    # with open("{0}.hack".format(input_file), "w") as resulting_file:
    for i in range(2):
        if i == 0: # first run
            while parsed.has_more_cmds():
                if parsed.command_type() == "C_COMMAND" or parsed.command_type() == "A_COMMAND":
                    rom_address += 1
                elif parsed.command_type() == "L_COMMAND":
                    st.add_entry(parsed.symbol(), rom_address + 1)
                parsed.advance()
            print st.table
        else: #second run
            rom_address = 0
            while parsed.has_more_cmds():
                if parsed.command_type() == "A_COMMAND":
                    if parsed.cc_is_symbol():
                        if st.contains(parsed.cc()):
                            cc = st.get_address(parsed.cc())
                        elif not st.contains(parsed.cc()):
                            st.add_entry(parsed.cc(), ram_address)
                            ram_address += 1
                parsed.advance()
