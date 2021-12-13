from tree import Tree

def test_size():
    tree = Tree()
    assert tree.size() == 1

def test_touch():
    tree = Tree()
    tree.touch("first.txt", 10)
    assert tree.size() == 11
    assert tree.ls() == ["f: first.txt"]

def test_mkdir():
    tree = Tree()
    tree.mkdir("second")
    assert tree.size() == 2
    assert tree.ls() == ["d: second"]

def test_cd():
    tree = Tree()
    tree