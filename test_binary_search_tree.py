# The main code to test the methods of BST functionality

import nlineards

if __name__ == '__main__':
    obj_bst = nlineards.BinarySearchTree()

    while True:
        inp = input("Press 0: exit, 1: Insert Node, 2: In Order Traversal, 3: Height?, 4: Is Empty?, 5: Size? : ")

        if(int(inp) == 0):
            break
        elif(int(inp) == 1):
            num = input("Enter no to Insert Node : ")
            obj_bst.insert_node(obj_bst.root,int(num))
        elif(int(inp) == 2):
            obj_bst.traverse_in_order(obj_bst.root)
            
        elif(int(inp)==3):
            print("Height of the tree is :", obj_bst.height(obj_bst.root))
               
        elif(int(inp) == 4):
            print("Is tree empty ?: ", obj_bst.is_empty())
        elif(int(inp)==5):
            print("no of elements in tree is: ", obj_bst.size())
        else:
            print("Press 0: exit, 1: Insert Node, 2: In Order Traversal, 3: Height?, 4: Is Empty?, 5: Size? : ")
    
