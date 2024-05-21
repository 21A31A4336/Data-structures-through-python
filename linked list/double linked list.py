class node:
    def __init__(self,data):
        self.data=data 
        self.next=None
        self.prev=None
class double_linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_start(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=self.tail=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def insert_end(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode
    def display_forward(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
    def display_backward(self):
        current=self.tail

        while current:
            print(current.data,end="->")
            current=current.prev
    def insert_position(self,data,position):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        elif position==1:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode

        else:
            current=self.head
            count=0
            while current:
                count+=1
                if count==position-1:
                    newnode.next=current.next
                    newnode.prev=current.prev
                    current.next=newnode
                    current.next.prev=newnode
                current=current.next
            if count<position-1:
                    self.insert_end(data)
    def delete_start(self):
        if self.head is None:
            print("empty")
        self.head=self.head.next
        self.tail=self.tail.next
    def delete_end(self):
        if self.head is None:
            print("empty")
        else:
            current=self.head
            while current.next.next:
                current=current.next
            current.next=None
        
           
obj=double_linked_list()
obj.insert_start(5)
obj.insert_start(8)
obj.insert_start(9)
obj.insert_start(1)
obj.display_forward()
obj.insert_position(6,5)
print()
obj.display_forward()
obj.delete_end()
print()
obj.display_forward()