from collections import deque
class Node:
    def __init__(self, data):
        assert data is not None
        self.data = data
    def __repr__(self):
        return "<Node: %s>"%repr(self.data)
    def __str__(self):
        return "<Node: %s>"%repr(self.data)
    def __lt__(self, obj):
        return self.data.demerits < obj.data.demerits

class LinkedList(deque):
    def appendleft(self, node):
        node.prev = None
        if self:
            node.next = self[0]
            self[0].prev = node
        else:
            node.next = None
        deque.appendleft(self, node)

    def insert(self, i, new_node):
        if i==0:
            self.appendleft(new_node)
        else:
            old  = self[i-1]
            if i==len(self):
                new_node.next = None
            else:
                new_node.next = self[i]
                self[i].prev = new_node
            new_node.prev = old
            old.next = new_node
            deque.insert(self, i, new_node)

    def append(self, new_node):
        i = len(self)
        self.insert(i, new_node)

    def insertBefore(self, existing, new_node):
        i = self.index(existing)
        self.insert(i, new_node)

    def remove(self, node):
        i = self.index(node)
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        deque.remove(self, node)

