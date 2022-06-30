def rotateQueue(q, n):
    if q.size() == 0:
        return
    for i in range(n):
        q.enqueue(q.dequeue())
