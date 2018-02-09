from __future__ import print_function
from BST import BST
from BST import size


def inOrderTrav(_BT):
    # TODO: add code here
    if _BT is not None:
        for re in inOrderTrav(_BT.l_child):
            yield re
        yield _BT.node
        for er in inOrderTrav(_BT.r_child):
            yield er


def Permutation(_BT, size1):
    # TODO: add code here
    if((_BT is not None) and (size1 != size(BT))):
        Permutation(_BT.l_child, size1)
        for index in range(size1):
            if index is 0:
                print(_BT.node, end='')
            for inx in range(size(BT)):
                if inOrderTrav(_BT) is not _BT.node:
                    print(inOrderTrav(_BT), end='')
        print()
        Permutation(_BT.r_child, size1)


BT = BST(1)
BT.insert(2)
BT.insert(3)
BT.insert(4)
BT.insert(5)
for i in range(size(BT)):
    Permutation(BT, i)
