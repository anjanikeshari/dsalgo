
## Stack implementation

# LIFO Stack implementation using a python list (dynamic array)

# Stack() creates a new empty stack

class Stack:
	def __init__(self):
		self.items = []

# isEmpty() bool
	def isEmpty(self):
		return self.items == []

# push(item) add to stack
	def push(self, item):
		self.items.append(item)

# size() return item size
	def size(self):
		return len(self.items)


# pop() removes item from the top
# Raise exception if the queue is empty.
	def pop(self):
		if (self.size() > 0):
			itemPopped = self.peek()
			self.items.pop()
			return itemPopped
						
		else:
			raise IndexError('Stack is empty')
			
# peek() shows you the top but does not remove
	def peek(self):
		return self.items[len(self.items)-1]

    


## Queue Implementation

# FIFO Queue implementation using linked list 

## Class Queue
class Queue:
  
##---Node has two part ---##
#     - Element to be stored
#     - Ref to next node

    ## Node Class
    class Node:

        #Initialization with Constructor for Node class
        def __init__(self, element):
            self.element = element    
            self.next = None   
 
    ##-- methods or function definitions --##

    #Initialization with Constructor for Queue Class
    # create an empty queue
    def __init__(self):
        self._size = 0        # Accounts for size of queue
        self.head = None      # Head of Queue
        self.tail = None      # Tail of Queue

    
    # Add new element new_elem to the rear of the queue
    def enqueue(self, element):
        new_elem = self.Node(element)
 
        if self.isEmpty():
            self.head = new_elem
        else:
            self.tail.next = new_elem
        self.tail = new_elem
        self._size += 1
 
    # Remove and return the first element from the queue
    # (i.e., FIFO). Raise exception if the queue is empty.
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
 
        element_dequeued = self.head.element
        self.head = self.head.next
        self._size -= 1
        if self.is_empty():
            self.tail = None
 
        return element_dequeued    

    # Return (but do not remove) the element at the front of
    # the queue. Raise exception if the queue is empty.
    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue is empty')
        return self.head.element

    # Return True if the queue is empty.
    def isEmpty(self):
        return self._size == 0
 
    # Return the number of elements in the queue.
    def size(self):
        return self._size


# A deque is a double-ended queue
# Also has a front and an end and the items are position within the collection
# Unrestrictive nature for adding items - add to front OR rear!
# Same for removal
# Does not require LIFO/FIFO enforced data structure design

#Implement a deque

# Deque() create a deque object
# addFront(item)
# addRear(item)
# removeFront()
# removeRear()
# peekRear()
# peekFront()
# isEmpty()
# size()

class Deque:
  
##---Node has two part ---##
#     - Element to be stored
#     - Ref to next node
#     - Ref to prev node

    ## Node Class (Doubly linked list implementation)
    class Node:  

        #Initialization with Constructor for Node class
        def __init__(self, element):
            self.element = element    
            self.next = None   
            self.prev = None

    ##-- methods or function definitions --##

    #Initialization with Constructor for Queue Class
    # create an empty queue
    def __init__(self):
        self._size = 0        # Accounts for size of queue
        self.head = None      # Head of Queue
        self.tail = None      # Tail of Queue
 
    # Return True if the queue is empty.
    def isEmpty(self):
        return self._size == 0
 
    # Return the number of elements in the queue.
    def size(self):
        return self._size
    
    # Add the entry from front (No FIFO LIFO)
    # Raise exception if the queue is empty.
    def addFront(self, element):
        new_elem = self.Node(element)
 
        if self.isEmpty():
            self.head = new_elem
            self.tail = new_elem
        else:
            new_elem.next  = self.head
            self.head.prev = new_elem
            self.head      = new_elem
            
        
        self._size += 1

    # Add the entry from front (No FIFO LIFO)
    # Raise exception if the queue is empty.
    def addRear(self, element):
        new_elem = self.Node(element)
 
        if self.isEmpty():
            self.head = new_elem
            self.tail = new_elem
        else:
            new_elem.prev = self.tail
            self.tail.next = new_elem
            self.tail = new_elem

        self._size += 1

    def removeFront(self):
        if self.isEmpty():
            raise IndexError('Deque is empty')
        elif self._size == 1:
            item_removed = self.head.element
            self.head = None
            self.tail = None
        else:
            item_removed = self.head.element
            temp = self.head
            
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self._size -= 1    
        return item_removed       

    def removeRear(self):
        if self.isEmpty():
            raise IndexError('Deque is empty')
        elif self._size == 1:
            item_removed = self.head.element
            self.head = None
            self.tail = None
        else:
            item_removed = self.tail.element
            temp = self.tail 
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self._size -= 1
        return item_removed

    # Return (but do not remove) the element at the front of
    # the queue. Raise exception if the queue is empty.
    def peekFront(self):
        if self.isEmpty():
            raise IndexError('Deque is empty')
        return self.tail.element

    # Return (but do not remove) the element at the front of
    # the queue. Raise exception if the queue is empty.
    def peekRear(self):
        if self.isEmpty():
            raise IndexError('Deque is empty')
        return self.head.element

    