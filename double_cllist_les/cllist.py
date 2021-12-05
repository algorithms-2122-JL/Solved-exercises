class _Node:
    def __init__(self, prevNode, nextNode, element):
        self.__prev = prevNode
        self.__next = nextNode
        self.__element = element
    
    def get(self):
        return self.__element

    def next(self):
        return self.__next
    
    def prev(self):
        return self.__prev
    
    def setNext(self, node):
        self.__next = node
        
    def setPrev(self, node):
        self.__prev = node

class CircularLinkedList:
    def __init__(self):
        self.__cursor = None
    
    def isEmpty(self):
        return self.__cursor is None

    def addLeft(self, element):
        if self.isEmpty():
            node = _Node(None, None, element)
            self.__cursor = node
            node.setNext(node)
            node.setPrev(node)
        else:
            node = _Node(self.__cursor.prev(), self.__cursor,element)
            self.__cursor.prev().setNext(node)
            self.__cursor.setPrev(node)
        return self
    
    def left(self):
        self.__cursor = self.__cursor.prev()
        return self

    def addRight(self, element):
        if self.isEmpty():
            node = _Node(None, None, element)
            self.__cursor = node
            node.setNext(node)
            node.setPrev(node)
        else:
            node = _Node(self.__cursor, self.__cursor.next(),element)
            self.__cursor.next().setPrev(node)
            self.__cursor.setNext(node)
        return self

    def right(self):
        self.__cursor = self.__cursor.next()
        return self

    def getCursor(self):
        return self.__cursor.get()

    def size(self):
        hopping_cursor = self.__cursor
        count = 0
        if self.isEmpty():
            return count
        else:
            hopping_cursor = hopping_cursor.next()
            count += 1
            while hopping_cursor is not self.__cursor:
                hopping_cursor = hopping_cursor.next()
                count += 1
        return count
        # def count(n, node):
        #     if node is self.__cursor:
        #         return n
        #     else:
        #         return count(n+1, node.right())
        
        # if self.isEmpty():
        #     return 0
        # else:
        #     return count(0, self.right())

    def removeLeft(self):
        temp = self.__cursor.prev()
        self.__cursor.prev().prev().setNext(self.__cursor)
        self.__cursor.setPrev(self.__cursor.prev().prev())
        return temp

    def removeRight(self):
        pass