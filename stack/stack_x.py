from stack import Stack


def paren_balanced(src):
    s = Stack()
    for c in src:
        if c == "(":
            s.push(1)
        elif s.size() > 0:
            s.pop()
        else:
            return False
    return s.size() == 0


def stack_eval(src):
    dest = Stack()
    while src.size() > 0:
        s = src.pop()
        if s == "=":
            break
        f = _funcs.get(s)
        if f is None:
            dest.push(s)
        else:
            a = dest.pop()
            b = dest.pop()
            dest.push(f(a, b))
    return dest.pop()

_funcs = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}
