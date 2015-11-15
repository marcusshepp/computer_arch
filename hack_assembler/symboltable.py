class SymbolTable(object):

    def __init__(self):
        """ Create new symbol table. """
        self.table = {}
        self.table["SP"] = 0
        self.table["LCL"] = 1
        self.table["ARG"] = 2
        self.table["THIS"] = 3
        self.table["THAT"] = 4
        self.table["R0"] = 0
        self.table["R1"] = 1
        self.table["R2"] = 2
        self.table["R3"] = 3
        self.table["R4"] = 4
        self.table["R5"] = 5
        self.table["R6"] = 6
        self.table["R7"] = 7
        self.table["R8"] = 8
        self.table["R9"] = 9
        self.table["R10"] = 10
        self.table["R11"] = 11
        self.table["R12"] = 12
        self.table["R13"] = 13
        self.table["R14"] = 14
        self.table["R15"] = 15
        self.table["SCREEN"] = 16384
        self.table["KBD"] = 24576

    def add_entry(self, symbol, address):
        """
        Adds the pair to the table.
        """
        self.table[symbol] = address

    def contains(self, symbol):
        """ Does the symbol table contain this value? """
        b = False
        if symbol in self.table:
            b = True
        return b

    def get_address(self, symbol):
        """
        Returns the address associated with the symbol.
        """
        return self.table.get(symbol, 0)
