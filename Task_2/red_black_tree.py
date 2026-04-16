"""Red Black Tree"""

#Code is from https://www.geeksforgeeks.org/dsa/introduction-to-red-black-tree/

#Function of Code: Insert values in to the tree, and make sure the Red Black Tree rules are kept. Recoloting
#and rotations are used to achieve this. 

class Node:
    def __init__(self, data):
        self.data = data
        self.color = "RED"   # "RED" or "BLACK"
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    # --- Rotations ---

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    # --- Fix Insert ---

    def fix_insert(self, k):
        while k != self.root and k.parent.color == "RED":
            if k.parent == k.parent.parent.left:
                uncle = k.parent.parent.right

                if uncle.color == "RED":
                    k.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)

                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
            else:
                uncle = k.parent.parent.left

                if uncle.color == "RED":
                    k.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)

                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)

        self.root.color = "BLACK"

    # --- Insert ---

    def insert(self, data):
        node = Node(data)
        node.left = self.NIL
        node.right = self.NIL

        parent = None
        current = self.root

        # BST insert
        while current != self.NIL:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if parent is None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

        # Fix colors
        if node.parent is None:
            node.color = "BLACK"
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    # --- Inorder Traversal ---

    def inorder(self, node, result=None):
        if result is None:
            result = []

        if node != self.NIL:
            self.inorder(node.left, result)
            result.append(f"{node.data}({node.color})")
            self.inorder(node.right, result)

        return result


# ---------------- MAIN ----------------

rbt = RedBlackTree()
rbt.insert(10)
rbt.insert(20)
rbt.insert(30)
rbt.insert(15)

traversal = rbt.inorder(rbt.root)
print("Inorder Traversal ->", " ".join(traversal))