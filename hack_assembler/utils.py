################################################
# Utilities
#
# Used to make other code look easier to read.
#
################################################
import sys

def create_file(ml, name):
    with open("{0}.hack".format(name), "w") as resulting_file:
        for line in ml:
            if str(line) != "None": # darn Labels
                resulting_file.write(str(line))
                resulting_file.write("\n")
        resulting_file.close()
    print "Resulting Machine Code Located: {0}.hack".format(name)


def no_file_arg():
    message = """
    \n
Please supply a relative file path to a `*.asm` file.
    \n
    """
    print message
    sys.exit()
