import sys
sys.path.append('../BST_python')
import BSTNode as BST

class Dictionary:
    def __init__(self):
        self.tree = None

    def is_empty(self):
        return (self.tree == None)

    def contains(self, key):
        return BST.search(self.tree, key)

    def insert(self, key, data):
        if (self.is_empty()):
            self.tree = BST.BSTNode(key, data)
        else:
            if (self.contains(key)):
                node = BST.search(self.tree, key)
                node.set_data(data)
            else:
                BST.insert(self.tree, BST.BSTNode (key, data))
    
    def lookup(self, key):
        node = self.contains(key)
        if (node != None):
            return node.get_data()
        else:
            return None

d = Dictionary()
d.insert(1, "test1")
d.insert(2, "test2")
d.insert(3, "test3")
d.insert(2, "test4")

print (d.lookup(2))