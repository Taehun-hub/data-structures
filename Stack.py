class Stack:
    def __init__(self):
        self.items = []

    def push(self,val):
        self.items.append(val) # O(1) 상수시간

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty") # O(1) 상수시간

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty") # O(1) 상수시간

    def __len__(self):
        return len(self.items) # O(1) 상수시간