# Data-structures-through-python
Data Structures Operations
This repository contains Python implementations of fundamental data structures, including stacks, queues, linked lists, and doubly linked lists. Each data structure offers various operations for efficient manipulation of data.

Stack Operations:
A stack is a Last-In-First-Out (LIFO) data structure that supports two main operations: push (adds an element to the top of the stack) and pop (removes the top element from the stack). Additionally, it provides operations like peek (returns the top element without removing it) and isEmpty (checks if the stack is empty).

Features
Push: Add an element to the top of the stack.
Pop: Remove and return the top element from the stack.
Peek: Return the top element without removing it.
isEmpty: Check if the stack is empty.
Usage
Creating a Stack:
python
Copy code
stack = Stack()
Pushing Elements:
python
Copy code
stack.push(5)
stack.push(10)
Popping Elements:
python
Copy code
top_element = stack.pop()
Queue Operations
A queue is a First-In-First-Out (FIFO) data structure with two primary operations: enqueue (adds an element to the back of the queue) and dequeue (removes and returns the front element from the queue). It also supports operations like peek (returns the front element without removing it) and isEmpty (checks if the queue is empty).

Features
Enqueue: Add an element to the back of the queue.
Dequeue: Remove and return the front element from the queue.
Peek: Return the front element without removing it.
isEmpty: Check if the queue is empty.
Usage
Creating a Queue:
python
Copy code
queue = Queue()
Enqueuing Elements:
python
Copy code
queue.enqueue(5)
queue.enqueue(10)
Dequeuing Elements:
python
Copy code
front_element = queue.dequeue()
Linked List Operations
A linked list is a linear data structure consisting of nodes, where each node contains data and a reference (or link) to the next node in the sequence. Operations include insertion, deletion, traversal, and searching.

Features
Insertion: Add an element to the linked list.
Deletion: Remove an element from the linked list.
Traversal: Visit each element in the linked list.
Searching: Find a specific element in the linked list.
Usage
Creating a Linked List:
python
Copy code
linked_list = LinkedList()
Inserting Elements:
python
Copy code
linked_list.insert(5)
linked_list.insert(10)
Deleting Elements:
python
Copy code
linked_list.delete(5)
Doubly Linked List Operations
A doubly linked list is a variation of the linked list in which each node has two references: one to the next node and another to the previous node. Operations are similar to those of a singly linked list but with the added capability of traversing backward.

Features
Insertion: Add an element to the doubly linked list.
Deletion: Remove an element from the doubly linked list.
Traversal: Visit each element in the doubly linked list forward or backward.
Searching: Find a specific element in the doubly linked list.
Usage
Creating a Doubly Linked List:
python
Copy code
doubly_linked_list = DoublyLinkedList()
Inserting Elements:
python
Copy code
doubly_linked_list.insert(5)
doubly_linked_list.insert(10)
Deleting Elements:
python
Copy code
doubly_linked_list.delete(5)
Note
These implementations are for educational purposes and demonstrate the basic operations of each data structure. In real-world applications, consider using built-in data structures provided by Python's standard library or optimized third-party libraries for better performance and reliability.
