"""
    WISP

    This is just a learning experience where I explore compiler design
"""

import os
import sys

import include.wisp


def main():
    fname = sys.argv[1]
    if extenCheck(fname) == True:
        pass
    else: 
        return
    oname = sys.argv[2]

    iF = open(sys.argv[1], "r")
    f = open("{}.asm".format(fname), "w+")
     
    asm_bp = "BITS 64\n%define SYS_EXIT 60\n\nsegment .text\n   global _start\n_start:\n"
    asm_exit = "   mov rax, SYS_EXIT\n   syscall"
    asm_ops = [
                asm_bp,
                eval_math(iF.read()),
                asm_exit
              ]

    f.writelines(asm_ops)
    iF.close()
    f.close()
    os.system("yasm -felf64 -o {}.o {}.asm".format(oname,fname))
    os.system("ld -o {} {}.o".format(oname,oname))
    os.system("rm {}.asm {}.o".format(fname,oname))


def extenCheck(s):
    return s.split(".")[1] == "wisp"


if __name__ == "__main__":
    main()
