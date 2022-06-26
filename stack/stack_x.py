from stack import Stack


def paren_balanced(src):
    s = Stack()
    for c in src:
        if c == "(":
            s.push(1)
        elif s.peek() is not None:
            s.pop()
        else:
            return False
    return s.peek() is None


def stack_eval(src):
    dest = Stack()
    while src.peek() is not None:
        s = src.pop()
        if s == "=":
            break
        elif s == "+":
            a = dest.pop()
            b = dest.pop()
            dest.push(a + b)
        elif s == "-":
            a = dest.pop()
            b = dest.pop()
            dest.push(a - b)
        elif s == "*":
            a = dest.pop()
            b = dest.pop()
            dest.push(a * b)
        elif s == "/":
            a = dest.pop()
            b = dest.pop()
            dest.push(a / b)
        else:
            dest.push(s)
    return dest.pop()
