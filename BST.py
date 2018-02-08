class BST:
    # initializes the Binary Search Tree (BST) class
    def __init__(self, data=None):
        self.node = data
        # optional (can initialize with root node)
        self.l_child = None
        self.r_child = None

    def insert(self, data=None):
        # inserts values from a list into the Binary Search Tree
        # then we check if the data value is None or if the index is greater than the array's length to end the code
        if data is None:
            pass
        # checks if root node is available (only ever works if you didn't put anything in the initialization)
        elif self.node is None:
            self.node = data
        # checks if it is less than the current node's value
        elif data <= self.node:
            # then checks if it is available and then continues with the code recursively
            if self.l_child is None:
                self.l_child = BST(data)
            # else it goes to the left child while making sure that the index is the array length so that the code will end immediately after the data is inputted
            else:
                self.l_child.insert(data)
        # checks if it is less than the current node's value
        elif data > self.node:
            # then checks if it is available and then continues with the code recursively
            if self.r_child is None:
                self.r_child = BST(data)
            # else it goes to the right child while making sure that the index is the array length so that the code will end immediately after the data is inputted
            else:
                self.r_child.insert(data)


def height(_BST):
    # gains the height of the BST
    if _BST is not None:
        if _BST.l_child is not None or _BST.r_child is not None:
            L = 1 + int(height(_BST.l_child))
            R = 1 + int(height(_BST.r_child))
            if L > R:
                return L
            else:
                return R
            # returns the height whether it be L or R depending on which is larger
        elif _BST.r_child is None and _BST.l_child is None:
            return 0
        else:
            return 1
    else:
        return 0


def size(_BT):
    if _BT is not None:
        return 1 + size(_BT.l_child) + size(_BT.r_child)
    else:
        return 0


def _miniValue(subtree):
    if subtree.l_child is None:
        return subtree.node
    else:
        return _miniValue(subtree.l_child)


def _maxiValue(subtree):
    if subtree.r_child is None:
        return subtree.node
    else:
        return _maxiValue(subtree.r_child)


def search(subtree, value):
    if subtree is None:
        return False
    if subtree.node is value:
        return True
    else:
        return search(subtree.l_child, value) or search(subtree.r_child, value)


T = BST(5)
T.insert(6)
T.insert(8)
T.insert(7)
T.insert(9)
T.insert(2)
T.insert(3)
T.insert(4)
T.insert(1)
print(height(T))
print(_miniValue(T))
print(_maxiValue(T))
print(search(T, 5))
print(search(T, 1))
print(search(T, 0))
