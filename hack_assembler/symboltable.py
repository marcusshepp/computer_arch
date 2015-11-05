class SymbolTable(object):

    def __init__(self):
        """ Create new symbol table. """
        self.table = {}

    def add_entry(self, symbol, address):
        """
        Adds the pair to the table.
        """
        self.table[symbol] = address
<<<<<<< HEAD

=======
    
>>>>>>> 7497abd4e719d959e5f2f0b0d4338699786d7583
    def contains(self, symbol):
        """ Does the symbol table contain this value? """
        b = False
        if symbol in self.table:
            b = True
        return b
<<<<<<< HEAD

=======
    
>>>>>>> 7497abd4e719d959e5f2f0b0d4338699786d7583
    def get_address(self, symbol):
        """
        Returns the address associated with the symbol.
        """
        return self.table.get(symbol, 0)
