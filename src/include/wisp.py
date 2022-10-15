def asm_eval(src):
    pass

def eval_math(src):
    ops = src.split()
    ret = " mov rdi, {}\n".format(ops[0])
    index = 0

    for x in ops:
        if(index % 2) == 1:
            match x:
                case "+":
                    ret += "    add rdi, {}\n".format(ops[index + 1])
                case "-":
                    ret += "    sub rdi, {}\n".format(ops[index + 1])
        return ret

def lexer(src):
    pass
