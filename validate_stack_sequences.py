
# This is stack application problem
###############################################################
#                    Problem Statement
# Given two integer arrays pushed and popped each with distinct
# values, return true if this could have been the result of a 
# sequence of push and pop operations on an initially empty 
# stack, or false otherwise.
###############################################################

# The main code to validate balanced paranthesis using Stack class 

## Import Libraries ##
# -- linear Data Structures
import lineards

class Solution:
    def validateStackSequences(self, pushed, popped):
        
        ptr_popped = 0 # Pointer to element to be popped
        obj_stack = lineards.Stack()
        for i in range(len(pushed)):
            obj_stack.push(pushed[i])
            while True:
                
                if((popped[ptr_popped] in obj_stack.getItems()) and (obj_stack.getItems()[obj_stack.size()-1] == popped[ptr_popped])):
                    obj_stack.pop()
                    if ptr_popped < len(popped)-1:
                        ptr_popped += 1
                else:
                    break
                
        if obj_stack.size() > 0:
            return False
        else:
            return True
        
if __name__ == '__main__':
    sol = Solution()
    pushed = input("Enter pushed element sequence separated by comma: ")
    popped = input("Enter popped sequence separated by comma: ")
    pushed = pushed.split(",")
    popped = popped.split(",")
    out = sol.validateStackSequences(pushed, popped)
    if out == False:
        print("Pop sequence doesnt match pushed sequqnce")
    else:
        print("Pop sequqnce matches push sequence") 
        
