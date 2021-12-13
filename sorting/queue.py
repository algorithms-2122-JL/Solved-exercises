from dllist import DoubleLinkedList

class Queue:
    def __init__(self):
        self.__list = DoubleLinkedList()
    
    def isEmpty(self):
        return self.__list.isEmpty()

    def first(self):
        return self.__list.front()

    def enqueue(self, element):
        self.__list.addBack(element)

    def dequeue(self):
        return self.__list.removeFront()

    def size(self):
        return self.__list.size()
    
    def mergeSort(self):
        def merge(Q1, Q2, Q):
            while((not Q1.isEmpty()) and (not Q2.isEmpty())):
                if Q1.first() < Q2.first():
                    Q.enqueue(Q1.dequeue())
                else:
                    Q.enqueue(Q2.dequeue())
            while(not Q1.isEmpty()):
                Q.enqueue(Q1.dequeue())
            while(not Q2.isEmpty()):
                Q.enqueue(Q2.dequeue())
        n = self.size()
        if n < 2:
            return self
        # divide
        Q1 = Queue()
        Q2 = Queue()
        while(Q1.size() < n/2):
            Q1.enqueue(self.dequeue())
        while(not self.isEmpty()):
            Q2.enqueue(self.dequeue())
        # conquer
        Q1.mergeSort()
        Q2.mergeSort()
        # merge
        merge(Q1, Q2, self)
        return self

    def quickSort(self):
        n = self.size()
        if n < 2:
            return self
        pivot = self.first()
        # divide
        L = Queue()
        E = Queue()
        G = Queue()
        while(not self.isEmpty()):
            k = self.dequeue()
            if k < pivot:
                L.enqueue(k)
            elif k == pivot:
                E.enqueue(k)
            else:
                G.enqueue(k)
        # conquer
        L.quickSort()
        # E.quickSort() # keeps recursing on same numbers
        G.quickSort()
        # merge
        while(not L.isEmpty()):
            self.enqueue(L.dequeue())
        while(not E.isEmpty()):
            self.enqueue(E.dequeue())
        while(not G.isEmpty()):
            self.enqueue(G.dequeue())
        return self