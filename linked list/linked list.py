class node:
    def __init__(self,data):
        self.data=data 
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None
    def insert_start(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
    def insert_end(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=newnode
    def insert_position(self,data,position):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            count=0
            current=self.head
            while current:
                count+=1
                if current==position-1:
                    newnode.next=current.next
                    current.next=newnode
                current=current.next
            if count<position-1:
                    self.insert_end(data)
                    return
            
    def  search(self,value):
        current=self.head
        count=0
        while current.next:
            count+=1
            if(current.data)==value:
                print(f"{current.data} found at {count}")
                break
            current=current.next
        else:
            print("not found")
    def delete_start(self):
        if self.head is None:
            print("empty list")
            return
        self.head=self.head.next
    def delete_end(self):
        if self.head is None:
            print("empty list")
            return
        elif self.head.next is None:
            self.head=None
        else:
            current=self.head
            while current.next.next:
                current=current.next
            current.next=None
    def delete_value(self,value):
        if self.head is None:
            print("empty list")
            return
        elif self.head.data==value:
            self.head=self.head.next
        else:
            current=self.head
            while current.next and current.next.data!=value:
                current=current.next
            if current is None :
                print("no data found")
                return
            current.next=current.next.next
    def update_start(self,key):
        if self.head is None:
            print("no values to update")
        else:
            self.head.data=key
    def update_end(self,key):
        current=self.head
        while current.next:
            current=current.next
        current.data=key
obj=linked_list()
obj.insert_end(1)
obj.insert_end(2)
obj.insert_end(3)
obj.insert_end(4)
obj.insert_position(5,8)
obj.update_start(6)
obj.display()


