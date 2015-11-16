################################################
# Parser
# in: assembly file
# out: machine code
#
# Performs various tasks nessessary to output the correct
# commands. Can also be used to to retreieve information about
# the `current command`.
#
# example usage:
# from parser import Parser
# i = ["@foo", "bar=1", "sum"]
# p = Parser(i, True)
# p.cc()
# >> "foo"
################################################
import re
from code import Code as C


class Parser(object):
    """
    Encapsulates access to the input code. Reads an assembly
    language command, parses it, and provides convenient access to the
    command's components (fields and symbols). In addition,
    removes all white space and comments.
    """
    def __init__(self, in_, debug=False, b_reg=False):
        """
        Input file is passed to this object
        thought a command line arg.
        Pass all commands into an array.
        """
        self.command_index = 0
        if debug:
            self.cmds = in_
        else:
            with open(in_, "r") as code_file:
                self.cmds = [line.strip() for line in code_file]
                for index, line in enumerate(self.cmds):
                    line = re.sub(r"//.*$", "", line)
                    self.cmds[index] = re.sub(r"\s.*$", "", line)
            self.cmds = [line for line in self.cmds if line != ""]
        self.c = C()
        if b_reg:
            self.b_reg = b_reg
            self.pad = "110"
            self.b_is_dest = False # when b register in destination
        else:
            self.pad = "111"
        self.null = "000"

    def cc(self):
        """
        in: none
        out: current command
        """
        return self.cmds[self.command_index]

    def b_cc(self):
        """
        in: none
        out: modified current command with b reg
        """
        cc = self.cc()
        if "B" in cc:
            if "A" in cc:
                b = cc.find("B")
                eq = cc.find("=")
                if b < eq: # dest is b
                    self.pad = "110"
                    self.b_is_dest = True
                else: self.pad = "101"
            else:
                self.pad = "101"
            self.cmds[self.command_index] = cc.replace("B", "D")
        else:
            self.pad = "111"
        return self.cmds[self.command_index]

    def has_more_cmds(self):
        """
        in: none
        out: whether or not there are more commands
        """
        if len(self.cmds) >= (self.command_index + 1):
            return True
        else: return False

    def advance(self):
        """
        Reads the next command from the input and
        makes it the current command. Should be
        called only if `has_more_cmds` is true.
        Initially there is no command.
        :return: None
        """
        self.command_index += 1

    def reset(self):
        """
        Return back to position zero in commands.
        """
        self.command_index = 0

    def cc(self):
        """
        in: none
        out: string value of current command
        """
        return self.cmds[self.command_index]

    def command_type(self):
        """
        :return: type of current cmd:
        - A_COMMAND for @xxx where xxx is either a symbol
        or a decimal number.
        - C_COMMAND for dest=comp;jump
        - L_COMMAND for where xxx is a symbol.
        """
        cc = self.cmds[self.command_index]
        l_command = lambda i : i.find('(') != -1 and i.find(')') != -1
        a_command = lambda i : i.find('@') != -1
        c_command = lambda i : i.find("(") == -1 and i.find("@") == -1
        if l_command(cc):
            return "L_COMMAND"
        elif a_command(cc):
            return "A_COMMAND"
        elif c_command(cc):
            return "C_COMMAND"

    def cc_is_symbol(self):
        """
        True if current command is symbol else false
        """
        cc = self.cmds[self.command_index]
        m = re.search(r'\d+$', cc)
        jump = ";" in cc
        # if the string ends in digits
        # or has a semi
        if m or jump:
            return False
        else: return True

    def cc_is_int(self):
        """
        in: none
        out: bool is current command integer
        """
        cc = self.cmds[self.command_index]
        m = re.search(r'\d+$', cc)
        # if the string ends in digits
        contains_char = any([i.isalpha() for i in cc[1:]])
        if contains_char:
            return False
        elif m: return True

    def symbol(self):
        """
        :return: the symbol or decimal xxx of
        current cmd @xxx or (xxx). Should be called only when
        command_type() returns A_COMMAND or L_COMMAND.
        ie. "LOOP" or "i"
        """
        cc = self.cmds[self.command_index]
        cc = re.sub(r"\(", "", cc)
        cc = re.sub(r"\)", "", cc)
        cc = re.sub(r"@", "", cc)
        return str(cc)

    def dest(self):
        """
        :return: the dest mnemonic in the current C-command
        (8 possibilites). Should be called only when
        command_type() is C.
        """
        cc = self.cmds[self.command_index]
        find = re.compile(r"^[^=]*") # everything before "="
        dest = re.search(find, cc).group(0)
        return dest

    def comp(self):
        """
        :return: the comp mnemonic in the current C-command
        (28 possibilites). Should only be called when
        command_type() returns C.
        """
        cc = self.cmds[self.command_index]
        equals, semi = 0, 0
        comp = []
        for i, v in enumerate(cc):
            if v == "=":
                equals += (i + 1)
            elif v == ";":
                semi += i
        if "=" in cc and ";" in cc:
            for v in cc[equals:semi]:
                comp.append(v)
        elif "=" in cc:
            for v in cc[equals:]:
                comp.append(v)
        return "".join(comp)

    def jump(self):
        """
        :return: the jump mnemonic in the current C-command
        (8 possibilites). Should only be called when
        command_type() returns C.
        """
        cc = self.cmds[self.command_index]
        there = ";" in cc
        if not there:
            return False
        else:
            jump = []
            indextostart = cc.index(";") + 1
            for v in cc[indextostart:]:
                jump.append(v)
            return "".join(jump)

    def c_to_binary(self, line, cmdtype, symboltable):
        """
        converts a c command to binary
        in: current command, command type, symboltable
        out: binary equivelant
        """
        if cmdtype == "C_COMMAND":
            the_a_bit = self.a_bit_method(line)
            _semi = ";" in line
            equals = "=" in line
            if _semi and equals: # dest = comp ; jump
                return self.semi_eq(line)
            elif equals:
                return self.eq(line)
            elif _semi:
                return self.semi(line)
            elif not equals and not _semi:
                return self.comp_only(line)
            else:
                try:
                    int(line)
                    return self.a_int_to_binary(line)
                except ValueError:
                    return self.a_int_to_binary(self.c.comp(line))

    def semi_eq(self, line):
        """
        in: current command
        out: c command with semi and equals into binary
        """
        the_a_bit = self.a_bit_method(line)
        semi = line.find(";")
        equals = line.find("=")
        return self.pad + the_a_bit + self.c.comp(line[equals + 1: semi]) + self.c.dest(line[:equals]) + self.c.jump(line[semi + 1:])

    def eq(self, line):
        """
        in: current command
        out: c command with equals into binary
        """
        the_a_bit = self.a_bit_method(line)
        equals = line.find("=")
        if self.b_reg and self.b_is_dest:
            _dest = "000"
            self.b_is_dest = False
        else: _dest = self.c.dest(line[:equals])
        return self.pad + the_a_bit + self.c.comp(line[equals + 1:]) + _dest + self.null

    def semi(self, line):
        """
        in: current command
        out: c command with semi into binary
        """
        the_a_bit = self.a_bit_method(line)
        semi = line.find(";")
        try:
            return self.pad + the_a_bit + self.c.comp(line[:semi]) + "000" + self.c.jump(line[semi + 1:])
        except KeyError:
            return self.pad + the_a_bit + "000000" + self.c.dest(line[:semi]) + self.c.jump(line[semi + 1:])

    def a_int_to_binary(self, line):
        """
        in: current command
        out: a command with an integer value to binary.
        """
        number = str(line)
        if "@" in number:
            number = number[1:]
        number = str(bin(int(number)))[2:]
        diff = abs(len(number) - 16)
        pad = ["0" for count in range(diff)]
        pad = "".join(pad)
        return pad + number

    def a_bit_method(self, line):
        """
        in: current command
        out: a bit for a c command
        """
        num = line.find("M")
        if num == -1:
            return "0"
        else:
            if line.find("J") + 1 == num:
                return "0"
            return "1"

    def comp_only(self, line):
        """
        in: current command
        out: c command with a comp only instruction
        """
        return self.pad + self.c.comp(line) + self.null + self.null
