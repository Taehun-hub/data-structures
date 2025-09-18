n=int(input())
k=int(input())
class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0
    def enqueue(self,val):
        self.items.append(val)
    def dequeue(self):
        if self.front_index == len(self.items):
            print("Queue is empty")
        else:
            X=self.items[self.front_index]
            self.front_index += 1
            return X
Q=Queue()
for i in range(n):
    Q.enqueue(i+1)
while len(Q.items) - Q.front_index > 1:
    for _ in range(k-1):             # k-1번 회전
        Q.enqueue(Q.dequeue())
    removed = Q.dequeue()            # k번째 제거
    print("빠진 값:", removed)

# 마지막 남은 값 출력
print("마지막 남은 값:", Q.dequeue())
