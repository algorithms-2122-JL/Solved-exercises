from sllist import SingleLinkedList

class Stack:
    def __init__(self) -> None:
        self.__list = SingleLinkedList()
    
    def push(self, element):
        self.__list.prepend(element)
    
    def top(self):
        return self.__list.head()
    
    def pop(self):
        # get top
        element = self.top()
        self.__list = self.__list.tail()
        return element

    def isEmpty(self):
        return self.__list.isEmpty()