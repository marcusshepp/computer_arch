################################################
# Code
# in: `current command`
# out: int or binary representation of said `current command`
#
# Contains several tables of choices. These are mapped to
# either binary string or decimal integer representation of
# the given `current command`.
#
# example usage:
# from code import Code
# i = ["AMD"]
# cd = Code()
# cd.dest(i[0])
# >> "111"
################################################
class Code(object):
    """ Translates Hack assembly language mnemonics into binary codes. """

    def __init__(self):
        self.ml = bin

    def dest(self, mnemonic):
        """
        in: command
        out: 3 bits
        returns the binary code of the dest mnemonic.
        """
        choices = {"0": "000",
                    "M": "001",
                    "D": "010",
                    "MD": "011",
                    "A": "100",
                    "AM": "101",
                    "AD": "110",
                    "AMD": "111"}
        return choices[mnemonic]

    def comp(self, mnemonic):
        """
        in: command
        out: 7 bits
        returns the binary code of the comp mnemonic.
        """
        a = {}
        choices = {"M-D": 7, "D-M": 19, "M-1": 50, "1-M": 50, "-M": 51,
            "M+1": 55, "1+M": 55, "M+D":2, "D+M": 2,
            "D|M": 21, "M|D": 21,
            "D&M": 0, "M&D": 0,
            "!M": 49,
            "M": 48,
            "-1": 58, "D-1": 14, "1-D": 14,
            "A-1": 50, "1-A": 50, "D-A": 19, "A-D": 7, "-D": 15, "-A": 51,
            "D+1": 13, "1+D": 13, "A+1": 55, "1+A": 55, "D+A": 2, "A+D": 2,
            "D|A": 21, "A|D": 21,
            "D&A": 0, "A&D": 0,
            "!A": 49, "!D": 13,
            "0": 42, "1": 63, "D": 12, "A": 48}
        cmd = choices[mnemonic]
        if cmd == 0:
            return "000000"
        def pad(line):
            if len(line) < 6:
                line = list(line)
                while len(line) < 6:
                    line.insert(0, "0")
            return "".join(line)
        return pad(self.ml(choices[mnemonic])[2:])

    def jump(self, mnemonic):
        """
        in: command
        out: 3 bits
        returns the binary code of the jump mnemonic.
        """
        choices = {
            "0": "000",
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111",
        }
        return choices[mnemonic]
