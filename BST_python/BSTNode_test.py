import BSTNode as BST

def build_tree(l):
    tree = BST.BSTNode(l[0], "")
    for e in l[1:]:
        BST.insert(tree, BST.BSTNode(e, ""))
    return tree


tree = BST.BSTNode(12, "")

node5 = BST.BSTNode(5, "")
node18 = BST.BSTNode(18, "")
node2 = BST.BSTNode(2, "")
node9 = BST.BSTNode(9, "")
node15 = BST.BSTNode(15, "")
node19 = BST.BSTNode(19, "")
node13 = BST.BSTNode(13, "")
node17 = BST.BSTNode(17, "")

BST.insert(tree, node5)
BST.insert(tree, node18)
BST.insert(tree, node2)
BST.insert(tree, node9)
BST.insert(tree, node15)
BST.insert(tree, node19)
BST.insert(tree, node13)
BST.insert(tree, node17)

print(BST.inorder(tree))

tree2 = build_tree([12,5,18,2,9,15,19,13,17])
print(BST.inorder(tree2))