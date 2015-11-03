class SymbolTable(object):
    
    def __init__(self):
        """ Create new symbol table. """
        self.table = {}
    
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
        return self.table[symbol]