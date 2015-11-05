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
def to_binary(line, cmdtype, symboltable):
    pad = "111"
    if cmdtype == "C_COMMAND":
        null = "000"
        line = "M;JGT"
        a_bit = "1" if "M" in line else "0"
        semi = ";" in line
        equals = "=" in line
        if semi and equals: # dest = comp ; jump
            semi = line.find(";")
            equals = line.find("=")
            return pad + a_bit + c.comp(line[equals + 1: semi]) + c.dest(line[:equals]) + c.jump(line[semi + 1:])
        elif equals:
            equals = line.find("=")
            return pad + a_bit + c.comp(line[equals + 1:]) + c.dest(line[:equals]) + null
        elif semi:
            semi = line.find(";")
            return pad + a_bit + "000000" + c.comp(line[:semi]) + c.dest(line[semi + 1:])

        comp = c.comp(line)
        dest = c.dest(line)
        jump = c.jump(line)
        return pad + a_bit + comp + dest + jump



i = ["@0",
     "D=M",
     "@1",
     "D=D-M",
     "@OUTPUT_FIRST",
     "D;JGT",
     "@1",
     "D=M",
     "@OUTPUT_D",
     "0;JMP",
     "(OUTPUT_FIRST)",
     "@0",
     "D=M",
     "(OUTPUT_D)",
     "@2",
     "M=D",
     "(INFINITE_LOOP)",
     "@INFINITE_LOOP",
     "0;JMP"]
ML = {}
code_obj = Code()
st = SymbolTable()
# input_file = sys.argv[1]
parsed = Parser(i)
rom_address = 0

# with open("{0}.hack".format(input_file), "w") as resulting_file:
for incrementer in range(2):
    if incrementer == 0: # first pass
        while parsed.has_more_cmds():
            if parsed.command_type() == "C_COMMAND" or parsed.command_type() == "A_COMMAND":
                rom_address += 1
            elif parsed.command_type() == "L_COMMAND":
                st.add_entry(parsed.symbol(), rom_address + 1)
            parsed.advance()
        print st.table
        parsed.reset()
    elif incrementer == 1:
        i = 0
        while parsed.has_more_cmds():
            cc = parsed.cc()
            command_type = parsed.command_type()
            print cc
            print command_type
            if command_type == "A_COMMAND":
                if st.contains(cc):
                    ML[i] = "0" + str(bin(st.get_address(cc[1:])))[2:]
                else: ML[i] = "0" + str(bin(st.get_address(line)))[2:]
            else:
                symboltable = st
                ML[i] = to_binary(cc, command_type, symboltable)
            parsed.advance()
            i += 1
        for k, v in ML.items():
            print k, v
