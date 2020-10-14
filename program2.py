# Program 2

def hello(name):
    if name == "":
        print("hello \"" + name + "\"\t=> \"Hello, World!\"")
    elif name == None:
        print("hello \t\t=> \"Hello, World!\"")
    else:
        print("hello \"" + name + "\"\t=> \"Hello, " + name.capitalize() + "!\"")

hello("john")
hello("aliCE")
hello(None)
hello("")
