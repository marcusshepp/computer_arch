import sys

from code import Code
from parser import Parser
from symboltable import SymbolTable

code_obj = Code()
input_file = sys.argv[1]

with open("{0}.hack".format(input_file[:3]), "w"):
    parsed = Parser(input_file)
    while parsed.has_more_cmds():
        ct = parsed.command_type()
        if ct == "A_COMMAND" or ct == "L_COMMAND":
            symbol = parsed.symbol()
        else:
            dest = parsed.dest()
            comp = parsed.comp()
            jump = parsed.jump()
        parsed.advance()
