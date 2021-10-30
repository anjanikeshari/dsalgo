

 # Binary Search Tree Python implementation
class BinarySearchTree:
  
    ## This Node class creates an element and
    ## a reference to it's left and right children
    class Node:
        
        def __init__(self, element):
            self.element = element
            self.left = None  # reference to the left Child
            self.right = None  # reference to the right Child
 
# Methods
    # create an empty BST
    def __init__(self):
        self.root = None
        self._size = 0
 
    # Recursively add element e to the tree
    def insert_node(self, root, element):
        # If no root exists, set new Node as root
        if self.root == None:
            self.root = self.Node(element)
            self._size += 1
            return
 
        if element < root.element:
            if root.left == None:
                root.left = self.Node(element)
                self._size += 1
            else:
                self.insert_node(root.left, element)
        else:
            if root.right == None:
                root.right = self.Node(element)
                self._size += 1
            else:
                self.insert_node(root.right, element)
 
    # Recursively prints the values in tree in
    # ascending order. (We use In Order traverse for that)
    def traverse_in_order(self, root):
        if root != None:
            self.traverse_in_order(root.left)
            print(root.element, end=" ")
            self.traverse_in_order(root.right)
 
    # Returns the longest path from
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