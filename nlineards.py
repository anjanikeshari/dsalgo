

 # Binary Search Tree Python implementation
class BinarySearchTree:
  
    ## This Node class creates an element and
    ## a reference to it's left and right children
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