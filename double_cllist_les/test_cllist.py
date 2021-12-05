from cllist import CircularLinkedList

def test_isEmpty():
    cllist = CircularLinkedList()
    assert cllist.isEmpty()

def test_addLeft():
    cllist = CircularLinkedList()
    cllist.addLeft("1")
    assert not cllist.isEmpty()

def test_left():
    cllist = CircularLinkedList()
    cllist.addLeft("1")
    cllist.left()
    assert cllist.getCursor() == "1"

def test_addRight():
    cllist = CircularLinkedList()
    cllist.addRight("1")
    assert not cllist.isEmpty()

def test_right():
    cllist = CircularLinkedList()
    cllist.addRight("2")
    cllist.right()
    assert cllist.getCursor() == "2"

def test_add_multiple():
    cllist = CircularLinkedList()
    cllist.addLeft("1")
    cllist.addLeft("4")
    cllist.addLeft("3")
    cllist.addRight("2")
    assert cllist.getCursor() == "1"
    cllist.right()
    assert cllist.getCursor() == "2"
    cllist.right()
    assert cllist.getCursor() == "4"
    cllist.right()
    assert cllist.getCursor() == "3"
    cllist.right()
    assert cllist.getCursor() == "1"

def test_size():
    cllist = CircularLinkedList()
    assert cllist.size() == 0
    cllist.addLeft("1")
    cllist.addLeft("4")
    cllist.addLeft("3")
    cllist.addRight("2")
    assert cllist.size() == 4