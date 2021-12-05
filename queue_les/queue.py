from dllist import DoubleLinkedList

class Queue:
    def __init__(self) -> None:
        self.__list = DoubleLinkedList()

    def isEmpty(self):
        return self.__list.isEmpty()
    
    