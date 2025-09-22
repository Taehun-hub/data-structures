class Node:
    def __init__(self,key=None):
        self.key=key
        self.next=None
    def __srt__(self):
        return str(self.key)
a=Node(3)
b=Node(9)
c=Node(-1)
a.next=b
b.next=c 