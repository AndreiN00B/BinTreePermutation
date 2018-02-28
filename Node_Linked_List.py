class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    def add(self, item):
        _node = Node(item)
        _node.next = self.head
        self.head = _node
    def size(self):
        _next, count = self.head, 0
        while _next != None:
            count += 1
            _next = _next.next
        return count
    def search(self, item):
        _next = self.head
        while _next != None:
            if _next.data == item:
                return True
            _next = _next.next
        return False
    def remove(self, item = None):
        if item is None:
            data = self.head
            prev_data = self.head
            while data != None:
                if data.next == item:
                    prev_data.next = data.next
                prev_data, data = data, data.next
        else:
            data = self.head
            prev_data = self.head
            while data != None:
                if data.data == item:
                    prev_data.next = data.next
                prev_data, data = data, data.next
    def output(self):
        _node = self.head
        try:
            s = str(_node.data)
            _next = _node.next
            while _next is not None:
                s += str(_next.data)
                _next = _next.next
            return s
        except:
            raise Exception("Linked List is Empty")
