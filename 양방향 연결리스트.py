class Node:
    def __init__(self,key=None):
        self.key=key
        self.next=self
        self.prev=self

class Doubly LinkedList:
    def __init__(self):
        self.head=Node()
        self.size=0