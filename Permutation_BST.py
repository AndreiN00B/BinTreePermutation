from __future__ import print_function
from BST import BST
from BST import size
from BST import height
from Node_Linked_List import LinkedList


class Permute:
    def __init__(self, _BT):
        self.BT = _BT
        self.__size = 1
        self.tval_perms = LinkedList()
        self.tval_perms.add(True)
        self.perms = LinkedList()
        self.data = None
    def Permutate(self, _tval = None, _perm = None):
        if _tval is None and _perm is None:
            _tval = self.tval_perms.head
            _perm = self.perms.head
        data = Iterate_Tree(self.BT)
        index = 1
        while self.__size < size(self.BT):
            if self.__size > 0 and self.__size < size(BT):
                data = Iterate_Tree(self.BT, index)
                if _tval.data:
                    if self.perms.head is None or _perm is None:
                        self.perms.add(data)
                    else:
                        self.perms.remove()
                        self.perms.add(data)
                    self.__size += 1
                else:
                    self.__size += 1
                    self.Permutate(_tval, _perm)
                index += 1
    def Output(self):
        self.perms.output()


def Iterate_Tree(_BT, index = 0, search = None):
    global BT
    if _BT is not None or (_BT is not None and index <= height(BT)):
        if search is None:
            return Iterate_Tree(_BT.r_child, index + 1, search)
            return _BT.node
            return Iterate_Tree(_BT.l_child, index + 1, search)
        else:
            return Iterate_Tree(_BT.r_child, index + 1, search)
            if search is not _BT.node:
                return _BT.node
            return Iterate_Tree(_BT.l_child, index + 1, search)



def Iter_Tree(_BT):
    if(_BT is not None):
        for placeholder1 in Iter_Tree(_BT.r_child):
            yield placeholder1
        yield _BT.node
        for placeholder2 in Iter_Tree(_BT.l_child):
            yield placeholder2


BT = BST(1)
BT.insert(2)
BT.insert(3)
BT.insert(4)
P = Permute(BT)
P.Permutate()
P.Output()
