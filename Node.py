class Node:
    def __init__(self,key=None):
        self.key=key
        self.next=None
    def __srt__(self):
        return str(self.key)