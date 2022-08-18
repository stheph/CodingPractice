import BSTNode as BST

def build_tree(l):
    tree = BST.BSTNode(l[0], "")
    for e in l[1:]:
        BST.insert(tree, BST.BSTNode(e, ""))
    return tree

def test_create_bst():
    tree = BST.BSTNode(1, "")

    inorder = BST.inorder(tree) # [1]
    key = tree.get_key() # 1
    data = tree.get_data() # ""
    left_child = tree.get_left_child() # None
    right_child = tree.get_right_child() # None
    parent = tree.get_parent() # None

    assert ((inorder, key, data, left_child, right_child, parent) == ([1], 1, "", None, None, None))

def test_insert_left_node():
    tree = BST.BSTNode(2, "test2")
    node = BST.BSTNode(1, "test1")
    BST.insert(tree, node)

    inorder = BST.inorder(tree) # [1,2]

    key = tree.get_key() # 2
    data = tree.get_data() # "test2"
    left_child = tree.get_left_child() # node
    right_child = tree.get_right_child() # None
    parent = tree.get_parent() # None

    left_child_key = left_child.get_key() # 2
    left_child_data = left_child.get_data() # "test2"

    assert ((inorder, key, data, left_child, right_child, parent, left_child_key, left_child_data) \
        == ([1,2], 2, "test2", node, None, None, 1, "test1"))


def test_insert_right_node():
    tree = BST.BSTNode(1, "test1")
    node = BST.BSTNode(2, "test2")
    BST.insert(tree, node)

    inorder = BST.inorder(tree) # [1,2]

    key = tree.get_key() # 1
    data = tree.get_data() # "test1"
    left_child = tree.get_left_child() # None
    right_child = tree.get_right_child() # node
    parent = tree.get_parent() # None

    right_child_key = right_child.get_key() # 2
    right_child_data = right_child.get_data() # "test2"

    assert ((inorder, key, data, left_child, right_child, parent, right_child_key, right_child_data) \
        == ([1,2], 1, "test1", None, node, None, 2, "test2"))

if __name__ == "__main__":
    test_create_bst()
    print ("test_create_bst passed!")

    test_insert_left_node()
    print ("test_insert_left_node passed!")

    test_insert_right_node()
    print ("test_insert_right_node passed!")