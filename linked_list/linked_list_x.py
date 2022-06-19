from linked_list import Node, LinkedList

def addLinkedList(a, b):
    c = LinkedList()
    na = a.head
    nb = b.head
    while (na is not None) and (nb is not None):
        c.add_in_tail(Node(na.value + nb.value))
        na = na.next
        nb = nb.next
    if (na is not None) or (nb is not None):
        return None
    else:
        return c
