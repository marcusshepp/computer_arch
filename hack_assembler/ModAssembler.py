#!/usr/bin/python
##################################
# Alternate Hack assembler

# example usage:
# python ModAssembler.py <modified script name>.asm
#
##################################

import sys, os

from parser import Parser
from symboltable import SymbolTable
from utils import create_file, no_file_arg
# from .marcus import greatness

DEBUG = False
B_REG = True

def main(debug, b_reg):
    """
    in: bool debug, bool b register
    out: void
    """
    ML = []
    st = SymbolTable()
    if len(sys.argv) < 2:
        no_file_arg()
    input_file = sys.argv[1]
    name = os.path.splitext(input_file)[0]
    parsed = Parser(input_file, debug, b_reg)
    rom_address = 0
    ram_address = 16
    """
    First pass
    """
    while parsed.has_more_cmds():
        if parsed.command_type() == "C_COMMAND" or parsed.command_type() == "A_COMMAND":
            rom_address += 1
        elif parsed.command_type() == "L_COMMAND":
            st.add_entry(parsed.symbol(), rom_address)
        parsed.advance()
    parsed.reset()

    """
    Second pass
    """
    i = 0
    while parsed.has_more_cmds():
        cc = parsed.b_cc() # account for b reg
        command_type = parsed.command_type()
        if command_type == "A_COMMAND":
            """
            Handle A commands.
            """
            if st.contains(cc[1:]):
                ML.append(parsed.a_int_to_binary(st.get_address(cc[1:])))
            elif parsed.cc_is_int():
                ML.append(parsed.a_int_to_binary(cc))
            elif not st.contains(cc[1:]):
                st.add_entry(cc[1:], ram_address)
                ML.append(parsed.a_int_to_binary(str(st.get_address(cc[1:]))))
                ram_address += 1
        else:
            ML.append(parsed.c_to_binary(cc, command_type, st))
        parsed.advance()
        i += 1
    create_file(ML, name)


if __name__ == "__main__":
    main(DEBUG, B_REG)
