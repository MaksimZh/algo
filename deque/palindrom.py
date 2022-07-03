from deque import Deque

def isPalindrom(s):
    d = Deque()
    for c in s:
        d.addTail(c)
    while d.size() > 1:
        if d.removeFront() != d.removeTail():
            return False
    return True
