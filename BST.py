class BST:
    # initializes the Binary Search Tree (BST) class
    def __init__(self, data=None):
        self.node = data
        # optional (can initialize with root node)
        self.l_child = None
        self.r_child = None

    def insert(self, array, data=None, index=0):
        # inserts values from a list into the Binary Search Tree
        # first condition checks to see if we need to take a value out of the array
        if data is None and len(array) > index:
            data = array[index]
        # then we check if the data value is None or if the index is greater than the array's length to end the code
        if data is None or index > len(array):
            pass
        # checks if root node is available (only ever works if you didn't put anything in the initialization)
        elif self.node is None:
            self.node = data
            self.insert(array, None, index + 1)
        # checks if it is less than the current node's value
        elif data <= self.node:
            # then checks if it is available and then continues with the code recursively
            if self.l_child is None:
                self.l_child = BST(data)
                self.insert(array, None, index + 1)
            # else it goes to the left child while making sure that the index is the array length so that the code will end immediately after the data is inputted
            else:
                self.l_child.insert(array, data, len(array))
                self.insert(array, None, index + 1)
        # checks if it is less than the current node's value
        elif data > self.node:
            # then checks if it is available and then continues with the code recursively
            if self.r_child is None:
                self.r_child = BST(data)
                self.insert(array, None, index + 1)
            # else it goes to the right child while making sure that the index is the array length so that the code will end immediately after the data is inputted
            else:
                self.r_child.insert(array, data, len(array))
                self.insert(array, None, index + 1)


def size(_BT):
    if _BT is not None:
        return 1 + size(_BT.left) + size(_BT.right)
    else:
        return 0
