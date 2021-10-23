
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
            self.head.next = new_elem
            self.head = new_elem
        
        self._size += 1

    # Add the entry from front (No FIFO LIFO)
    # Raise exception if the queue is empty.
    def addRear(self, element):
        new_elem = self.Node(element)
 
        if self.isEmpty():
            self.head = new_elem
            self.tail = new_elem
        else:
            new_elem.next = self.tail
            self.tail = new_elem
        self._size += 1

    def removeFront(self, element):
        if self.isEmpty():
            raise IndexError('Deque is empty')
        elif self.size == 1:
            item_removed = self.head.element
            self.head = None
            self.tail = None
         else:
            item_removed = self.head.element
               



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



 # Binary Search Tree Python implementation
class BinarySearchTree:
  
    # This Node class creates an element and
    # a reference to it's left and right children
    class Node:
        
 
        def __init__(self, e):
            self.element = e
            self.left = None  # reference to the left Child
            self.right = None  # reference to the right Child
 
# Methods
    # create an empty BST
    def __init__(self):
        self.root = None
        self._size = 0
 
    # Recursively add element e to the tree
    def add_node(self, root, e):
        # If no root exists, set new Node as root
        if self.root == None:
            self.root = self.Node(e)
            self._size += 1
            return
 
        if e < root.element:
            if root.left == None:
                root.left = self.Node(e)
                self._size += 1
            else:
                self.add_node(root.left, e)
        else:
            if root.right == None:
                root.right = self.Node(e)
                self._size += 1
            else:
                self.add_node(root.right, e)
 
    # Recursively prints the values in tree in
    # ascending order. (We use In Order traverse for that)
    def traverse_in_order(self, root):
        if root != None:
            self.traverse_in_order(root.left)
            print(root.element, end=" ")
            self.traverse_in_order(root.right)
 
    # Returns the largest number of edges in a path from
    # root node of tree to a leaf node.
    def height(self, root):
        if root == None:
            return 0
 
        return max(self.height(root.left),
                   self.height(root.right)) + 1
 
    # Returns True if no elements found in tree,
    # else returns False
    def is_empty(self):
        return self._size == 0
 
    # Returns the number of elements in tree
    def size(self):
        return self._size