class stack:
    def __init__(self):
        self.stack=[]
        self.size=5
        self.top=-1
    def push(self,n):
        if self.top<self.size-1:
            self.top+=1
            self.stack.append(n)
        else:
            print("stack overflow!!!")
    def pop(self):
        if self.top==-1:
            print("stack underflow")
        else:
            self.stack.pop()
            self.top-=1
    def peek(self):
        print(self.stack[self.top])
    def display(self):
        print(self.stack)    
obj=stack()
obj.push(6)
obj.push(3)
obj.pop()
obj.display()