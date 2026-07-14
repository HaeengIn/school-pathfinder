import os


def clear():
    os.system("clr" if os.name == "nt" else "clear")
