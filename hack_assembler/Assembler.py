#!/usr/bin/python
##################################
# Hack assembly to Hack machine language
##################################

import sys, os

from parser import Parser
from symboltable import SymbolTable
from utils import create_file, no_file_arg

DEBUG = False

def main(debug):
    """
    in: bool debug
    out: void
    """
    ML = []
    st = SymbolTable()
    if len(sys.argv) < 2:
        no_file_arg()
    input_file = sys.argv[1]
    name = os.path.splitext(input_file)[0]
    parsed = Parser(input_file, debug)
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
    while parsed.has_more_cmds():
        cc = parsed.cc()
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
    create_file(ML, name)


if __name__ == "__main__":
    main(DEBUG)
