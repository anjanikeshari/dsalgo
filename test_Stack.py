# The main code to test the methods of Stack functionality

import lineards

if __name__ == '__main__':
    obj_stack = lineards.Stack()
    
    while True:
        
        
        inp = input("Press 0: exit, 1: push, 2: pop, 3: Is empty ?, 4: Stack size ? :")

        if(int(inp) == 0):
            break
        elif(int(inp) == 1):
            num = input("Enter no to push : ")
            obj_stack.push(int(num))
        elif(int(inp) == 2):
            item = obj_stack.pop()
            print("Item returned : " + str(item))

        elif(int(inp)==3):
            if obj_stack.isEmpty():
                print("Stack is empty")
            else:
                print("Stack not empty")
        elif(int(inp) == 4):
            print("Stack Size: ", obj_stack.size())    
        else:
            inp = input("Press 0: exit, 1: Enqueue, 2: Dequeue, 3: Is empty ?, 4: Queue size ? :")