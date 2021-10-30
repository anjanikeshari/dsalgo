# This is stack application problem
###############################################################
#                    Problem Statement
# Given a string A consisting only of '(' and ')'.
# You need to find whether parantheses in A is balanced or not 
# if it is balanced then return 1 else return 0.
###############################################################

# The main code to validate balanced paranthesis using Stack class 

## Import Libraries ##
# -- linear Data Structures
import lineards

class Solution:
    # @param input : string
    # @return a bool
    def solve(self, A):
        obj_stack = lineards.Stack()
        if len(A) > 0:      
            if A[0] == '(':
                for i in range(len(A)):
                    if A[i] == '(':
                        obj_stack.push('(')
                    elif A[i] == ')':
                        if obj_stack.size() > 0:
                            obj_stack.pop()
                        else:
                            return 0    
                
                if obj_stack.size() == 0:
                    return 1
                elif obj_stack.size() > 0:
                    return 0
            else:
                return 0
        else:
            return 1

if __name__ == '__main__':

    
    inp = input("Please input paranthesis string: ")

    sol = Solution()
    out = sol.solve(inp)
    if out == 1:
        print("Paranthesis is balanced")
    else:
        print("Paranthesis is not balanced")