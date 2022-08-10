
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
    
    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node
    
    def set_parent(self, node):
        self.parent = node

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

def predecessor(tree):
    # The largest key prior to the current key
    # In inorder traversal, the predecessor will be in the node's left child, since it goes left->parent->right
    x = tree
    if not (x.get_left_child() == None):
        return max(x.get_left_child())

    # If the node lacks a left child, then the predecessor will be the lowest ancestor who's right child is also an ancestor of the node
    # so we traverse up the tree, iteration stops when we encounter a node that's a right child instead of a left
    y = x.get_parent()
    while not (y == None) and x == y.get_left():
        x = y
        y = y.get_parent()
    return y

def successor(tree):
    # Symmetric to predecessor
    x = tree
    if not (x.get_right_child() == None):
        return min(x.get_right_child())
    
    y = x.get_parent()
    while not (y == None) and x == y.get_right():
        x = y
        y = y.get_parent()
    return y

def insert(tree, node):
    # Assumes no duplicate keys
    y = None # Parent of current node
    x = tree
    k = node.get_key()

    while not (x == None):
        y = x
        if k < x.get_key():
            # The node we're trying to insert has a key that's smaller, hence on the left
            x = x.get_left()
        else:
            # Else go right
            x = x.get_right()
    
    # y is now the node that will become the parent of 'node'
    node.set_parent(y)

    if y == None:
        # The tree was empty, so node becomes the root of the tree
        tree = node
    else:
        # Otherwise, just make the node the correct child of y
        if k < y.get_key():
            y.set_left_child(node)
        else:
            y.set_right_child(node)