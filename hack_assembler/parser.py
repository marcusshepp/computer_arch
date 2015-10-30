import re


class Parser(object):
    """
    Encapsulates access to the input code. Reads an assembly
    language command, parses it, and provides convenient access to the
    command's components (fields and symbols). In addition,
    removes all white space and comments.
    """
    def __init__(self, input_file):
        """
        Input file is passed to this object
        thought a command line arg.
        Pass all commands into an array.
        """
        self.command_index = 0
        with open(input_file, "r") as code_file:
            self.cmds = [line.strip() for line in code_file]
            for index, line in enumerate(self.cmds):
                line = re.sub(r"//.*$", "", line)
                self.cmds[index] = re.sub(r"\s.*$", "", line)
        self.cmds = [line for line in self.cmds if line != ""]
        print self.cmds
        self.current_cmd = self.cmds[self.command_index]

    def has_more_cmds(self):
        """
        Are there more commands in the input?
        :return: boolean
        """
        if len(self.cmds) <= (self.command_index + 1):
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

    def command_type(self):
        """
        :return: type of current cmd:
        - A_COMMAND for @xxx where xxx is either a symbol
        or a decimal number.
        - C_COMMAND for dest=comp;jump
        - L_COMMAND for where xxx is a symbol.
        """
        commands = {"@": "A_COMMAND",
                    "(": "L_COMMAND",
                    "M": "C_COMMAND",}
        if self.current_cmd[0] in commands: # pythonic solution?
            return commands[self.current_cmd[0]]
        elif self.current_cmd[0] == "D":
            return "C_COMMAND"

    def symbol(self):
        """
        :return: the symbol or decimal xxx of
        current cmd @xxx or (xxx). Should be called only when
        command_type() returns A_COMMAND or L_COMMAND.
        ie. "LOOP" or "i"
        """
        cc = self.current_cmd
        cc = re.sub(r"\(", "", cc)
        cc = re.sub(r"\)", "", cc)
        cc = re.sub(r"@", "", cc)
        return cc

    def dest(self):
        """
        :return: the dest mnemonic in the current C-command
        (8 possibilites). Should be called only when
        command_type() is C.
        """
        find = re.compile(r"^[^=]*") # everything before "="
        dest = re.search(find, self.current_cmd).group(0)
        return dest

    def comp(self):
        """
        :return: the comp mnemonic in the current C-command
        (28 possibilites). Should only be called when
        command_type() returns C.
        """
        cc = self.current_cmd
        equals, semi = 0
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
        cc = self.current_cmd
        jump = []
        the_index_to_start = 0
        for i, v in enumerate(cc):
            if v == ";":
                the_index_to_start = (i - 1)
        for v in cc[the_index_to_start:]:
            jump.append(v)
        return "".join(jump)
