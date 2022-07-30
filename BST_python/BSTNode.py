
class BSTNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
    
    def get_key(self):
        return self.key
    
    def get_data(self):
        return self.data

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def get_parent(self):
        return self.parent

def search(tree, key):
    if (tree == None) or (tree.get_key() == key):
        # It's not in the tree, or we found it
        return tree

    if key < tree.get_key():
        # If it's less than the current node's key, it'll be to the left, else to the right
        return search(tree.get_left_child(), key)
    else:
        return search(tree.get_right_child(), key)

def min(tree):
    # The smallest key is the furthest left node
    x = tree
    while not (x.get_left_child() == None):
        x = x.get_left_child()
    return x

def max(tree):
    # Opposite of min
    x = tree
    while not (x.get_right_child() == None):
        x = x.get_right_child()
    return x