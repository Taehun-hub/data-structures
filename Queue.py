class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0
    def enqueue(self,val):
        self.items.append(val)
    def dequeue(self):
        if slef.front_index == len(self.items):
            print("Queue is empty")
        else:
            X=self.items[front_index]
            slef.front_index += 1
            return X