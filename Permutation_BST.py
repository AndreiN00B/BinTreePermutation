from BST import BST
from BST import size


def Permutation(_BT):
    if _BT is not None:
        Permutation(_BT.left)
        # TODO: Add permutation code here.
        Permutation(_BT.right)


BT = BST()
BT.insert(1)
