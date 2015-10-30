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
        choices = {"null": 0,
                    "M": 1,
                    "D": 2,
                    "MD": 3,
                    "A": 4,
                    "AM": 5,
                    "AD": 6,
                    "AMD": 7}
        print "dest ML: ", self.ml(choices[mnemonic])[2:]
        return self.ml(choices[mnemonic])[2:]

    def comp(self, mnemonic):
        """
        in: command
        out: 7 bits
        returns the binary code of the comp mnemonic.
        """
        a = {}
        if "M" in mnemonic:
            if "-" in mnemonic:
                choices = {"M-D": 7, "D-M": 19, "M-1": 50, "-M": 51}
            elif "+" in mnemonic:
                choices = {"M+1": 55, "D+M": 2}
            elif "|" in mnemonic:
                choices = {"D|M": 21}
            elif "&" in mnemonic:
                choices = {"D&M": 0}
            elif "!" in mnemonic:
                choices = {"!M": 49}
            else:
                choices = {"M": 48}
        else:
            if "-" in mnemonic:
                choices = {"-1": 58, "D-1": 14, "A-1": 50, "D-A": 19, "A-D": 7, "-D": 15}
            elif "+" in mnemonic:
                choices = {"D+1": 13, "A+1": 55, "D+A": 2}
            elif "|" in mnemonic:
                choices = {"D|A": 21}
            elif "&" in mnemonic:
                choices = {"D&A": 0}
            elif "!" in mnemonic:
                choices = {"!A": 49}
            else:
                choices = {"0": 58, "1": 14, "D": 12, "A": 48}
        print "comp ML: ", self.ml(choices[mnemonic])[2:]
        return self.ml(choices[mnemonic])[2:]

    def jump(self, mnemonic):
        """
        in: command
        out: 3 bits
        returns the binary code of the jump mnemonic.
        """
        choices = {
            "null": 0,
            "JGT": 1,
            "JEQ": 2,
            "JGE": 3,
            "JLT": 4,
            "JNE": 5,
            "JLE": 6,
            "JMP": 7,
        }
        cmd = self.ml(choices[mnemonic])
        if cmd != 0:
            print "jump ML: ", self.ml(choices[mnemonic])[2:]
            return self.ml(choices[mnemonic])[2:]
        else: return self.ml(choices[mnemonic])