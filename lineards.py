
## Stack implementation

# Stack() creates a new empty stack

class Stack(object):
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
	def pop(self):
		if (self.size() > 0):
			print("Element popped")
			item = self.peek()
			self.items.pop()
			return item
						
		else:
			print("Stack is empty")
			return 'none'
# peek() shows you the top but does not remove
	def peek(self):
		return self.items[len(self.items)-1]





## Queue Implementation

class Queue(object):
# Queue() to create a queue	
	def __init__(self):
		self.items = []

# isEmpty() is the bool
	def isEmpty(self):
		return self.items == []

# enqueue(item) to add to the rear
	def enqueue(self, item):
		self.items.insert(0, item) # insert for FIFO

# dequeue() removes from the front
	def dequeue(self):
		if (self.size() > 0):
			print("Element Dequeued")
			item = self.getFrontElement()
			self.items.pop()
			return item
		else:
			print("Queue is empty")
			return 'none'
		
# size() returns the size
	def size(self):
		return len(self.items)

# getFrontElement() returns first element but does not remove
	def getFrontElement(self):
		return self.items[len(self.items)-1]