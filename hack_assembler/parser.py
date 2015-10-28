class Parser(object):
    """
    Encapsulates access to the input code. Reads an assembly
    language command, parses it, and provides convenient access to the 
    command's components (fields and symbols). In addition,
    removes all white space and comments.
    """
    def __init__(self, input_file):
        pass
    
    def has_more_cmds(self):
        """ 
        Are there more commands in the input?
        :return: boolean    
        """
        pass
    
    def advance(self):
        """ 
        Reads the next command from the input and 
        makes it the current command. Should be
        called only if `has_more_cmds` is true.
        Initially there is no command.
        :return: None
        """
        pass
    
    def command_type(self):
        """ 
        :return: type of current cmd:
        - A_COMMAND for @xxx where xxx is either a symbol
        or a decimal number.
        - C_COMMAND for dest=comp;jump
        - L_COMMAND for where xxx is a symbol.
        """
        pass
    
    def symbol(self):
        """
        :return: the symbol or decimal xxx of
        current cmd @xxx or (xxx). Should be called only when
        command_type() returns A_COMMAND or L_COMMAND.
        """
        pass
    
    def dest(self):
        """
        :return: the dest mnemonic in the current C-command
        (8 possibilites). Should be called only when
        command_type() is C.
        """
        pass
    
    def comp(self):
        """
        :return: the comp mnemonic in the current C-command
        (28 possibilites). SHould only be called when
        command_type() returns C.
        """
        pass
        
    def jump(self):
        """
        :return: the jump mnemonic in the current C-command
        (8 possibilites). SHould only be called when
        command_type() returns C.
        """
        pass