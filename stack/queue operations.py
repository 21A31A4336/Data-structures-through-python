class queue:
    def __init__(self):
        self.queue=[]
        self.size=5
        self.rear=self.front=-1
    def enqueue(self,data):
        if self.front!=self.rear or self.rear<self.size-1:
            self.rear+=1
            self.queue.append(data)
        else:
            print("stack overflow")
    def display(self):
        for i in range(self.front,self.rear):
            print(self.queue[i])
    def dequeue(self):
        if self.rear==-1:
            print("stack underflow")
        else:
            self.front+=1
            self.queue.pop(self.front)
    def peek(self):
        print(self.queue[self.front])
obj=queue()
obj.enqueue(5)
obj.enqueue(4)
obj.enqueue(3)
obj.enqueue(2)
obj.enqueue(1)
obj.dequeue()
obj.display()
