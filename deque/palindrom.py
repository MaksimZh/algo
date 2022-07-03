from deque import Deque

def isPalindrom(s):
    d = Deque()
    for c in s:
        d.addTail(c)
    for c in s:
        if d.removeTail() != c:
            return False
    return True
