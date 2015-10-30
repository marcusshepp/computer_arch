#!/usr/bin/python
import sys

from code import Code
from parser import Parser
from symboltable import SymbolTable


if __name__ == "__main__":
    code_obj = Code()
    input_file = sys.argv[1]
    ML = []
    # with open("{0}.hack".format(input_file), "w") as resulting_file:
    parsed = Parser(input_file)
    while parsed.has_more_cmds():
        print parsed.has_more_cmds()
        ct = parsed.command_type()
        print ct
        if ct == "A_COMMAND" or ct == "L_COMMAND":
            symbol = parsed.symbol()
            print symbol
        else:
            # C - Command
            dest = parsed.dest()
            print dest
            dest = code_obj.dest(dest)
            print dest
            ML.append(dest)
            comp = parsed.comp()
            print comp
            comp = code_obj.comp(comp)
            print comp
            ML.append(comp)
            jump = parsed.jump()
            print jump
            jump = code_obj.jump(jump)
            print jump
            ML.append(jump)
        parsed.advance()
    print "ML: ", ML
    for line in ML:
        print "line: ", line
        resulting_file.write(str(line))