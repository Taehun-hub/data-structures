class Node:
    def __init__(self,key=None):
        self.key=key
        self.next=None
    def __srt__(self):
        return str(self.key)

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    def PushFront(self,key):
        new_node=Node(key)
        new_node.next=L.head
        L.head=new_node
        L.size+=1
    def PushBack(self,key):
        V=Node(key)
        if len(self)==0:
            self.head=V
        else:
            tail=self.head
            while tail.next !=None:
                tail=tail.next
            tail.next=V
        self.size+=1
    def __len__(self):
        return self.size
    def popFront(self):
        if len(self)==0:
            return None
        else:
            X=self.head
            key=X.key
            self.head=X.next
            self.size-=1
            del X
            return key
    def popBack(self):
        if len(self)==0:
            return None
        else:
            prev,tail=None,self.head
            while tail.next!=None:
                prev,tail=tail,tail.next
            if len(self)==1:
                self.head=None
            else:
                prev.next=tail.next
            key=tail.key
            del tail
            self.size-=1
            return key
    def search(self,key):
        V=self.head
        while V !=None:
            if V.key==key:
                return V
            V=V.next
        return V
    def __iterator__(self):
        V=self.head
        while V!=None:
            yield V
            V=V.next
        return

