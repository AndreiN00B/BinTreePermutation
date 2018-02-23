from __future__ import print_function
from BST import BST
from BST import size
from Node_Linked_List import LinkedList
from Node_Linked_List import Node


def inOrderTrav(_BT):
    # TODO: add code here
    if _BT is not None:
        for re in inOrderTrav(_BT.l_child):
            yield re
        yield _BT.node
        for er in inOrderTrav(_BT.r_child):
            yield er


def Permutation(_BT, _size):
    global BT
    if(_BT is not None and _size < size(BT)):
        Permutation(_BT.l_child, _size)
        # TODO: add code here
        Permutation(_BT.r_child, _size)


BT = BST(1)
BT.insert(2)
BT.insert(3)
BT.insert(4)
for i in range(size(BT)):
    Permutation(BT, i, BT)
