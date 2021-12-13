from queue import Queue

def test_merge_sort():
    testqueue = Queue()
    assert testqueue.isEmpty()
    testqueue.enqueue(0.004)
    testqueue.enqueue(3.141592)
    testqueue.enqueue(15)
    testqueue.enqueue(7)
    testqueue.enqueue(12)
    testqueue.enqueue(4)
    testqueue.enqueue(11)
    testqueue.enqueue(13e6)
    testqueue.enqueue(400)
    testqueue.enqueue(67)
    testqueue.enqueue(333)
    testqueue.enqueue(9999)
    testqueue.enqueue(1.5e6)
    testqueue.enqueue(1.2)
    testqueue.enqueue(-78)
    testqueue.enqueue(3.6)
    assert testqueue.size() == 16
    testqueue.mergeSort()
    assert testqueue.dequeue() == -78
    assert testqueue.dequeue() == 0.004
    assert testqueue.dequeue() == 1.2
    assert testqueue.dequeue() == 3.141592

def test_quick_sort():
    testqueue = Queue()
    assert testqueue.isEmpty()
    testqueue.enqueue(0.004)
    testqueue.enqueue(3.141592)
    testqueue.enqueue(15)
    testqueue.enqueue(7)
    testqueue.enqueue(12)
    testqueue.enqueue(4)
    testqueue.enqueue(11)
    testqueue.enqueue(13e6)
    testqueue.enqueue(400)
    testqueue.enqueue(67)
    testqueue.enqueue(333)
    testqueue.enqueue(9999)
    testqueue.enqueue(9999)
    testqueue.enqueue(1.5e6)
    testqueue.enqueue(1.2)
    testqueue.enqueue(-78)
    testqueue.enqueue(3.6)
    assert testqueue.size() == 17
    testqueue.quickSort()
    assert testqueue.dequeue() == -78
    assert testqueue.dequeue() == 0.004
    assert testqueue.dequeue() == 1.2
    assert testqueue.dequeue() == 3.141592