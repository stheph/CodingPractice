
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

    def __str__(self):
        return "({0} : {1})".format(self.key, self.data)

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
    while not (y == None) and x == y.get_left_child():
        x = y
        y = y.get_parent()
    return y

def successor(tree):
    # Symmetric to predecessor
    x = tree
    if not (x.get_right_child() == None):
        return min(x.get_right_child())
    
    y = x.get_parent()
    while not (y == None) and x == y.get_right_child():
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
            x = x.get_left_child()
        else:
            # Else go right
            x = x.get_right_child()
    
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

def delete(tree, node):
    x = node
    y = node.get_parent()
    # node has no children, so we can simply replace it with None
    if x.get_left_child() == None and x.get_right_child() == None:
        if y.get_left_child() == x:
            y.set_left_child(None)
        else:
            y.set_right_child(None)

    # node has one child, so we remove it and set its child as its parent's child
    elif x.get_left_child() == None and x.get_right_child() != None:
        if y.get_left_child() == x:
            y.set_left_child(x.get_right_child())
        else:
            y.set_right_child(x.get_right_child())
        
    elif x.get_left_child() !=None and x.get_right_child() == None:
        if y.get_left_child() == x:
            y.set_left_child(x.get_left_child())
        else:
            y.set_right_child(x.get_left_child())

    # node has two children, so it's a little bit more complicated
    else:
        # we have to replace x with its successor, call it z
        z = successor(x)

        # z's parent inherit z's children (technically there should only be one)
        w = z.get_parent()
        w.set_left_child(z.get_left_child())
        w.set_right_child(z.get_right_child())

        # z gets node's children
        z.set_left_child(x.get_left_child())
        z.set_right_child(x.get_right_child())

        # y's child now becomes z
        if y.get_left_child() == x:
            y.set_left_child(z)
        else:
            y.set_right_child(z)

def inorder(tree):
    if tree == None:
        return []
    else:
        left = inorder(tree.get_left_child())
        current = [tree.get_key()]
        right = inorder(tree.get_right_child())
        return left + current + right