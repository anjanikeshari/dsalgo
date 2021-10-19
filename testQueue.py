# The main code to test the methods of Queue functionality


import lineards

if __name__ == '__main__':
    obj_Q = lineards.Queue()
    
    while True:
        inp = input("Press 0: exit, 1: Enqueue, 2: Dequeue, 3: Is empty ?, 4: Queue size ? :")

        if(int(inp) == 0):
            break
        elif(int(inp) == 1):
            num = input("Enter no to Enqueue : ")
            obj_Q.enqueue(int(num))
        elif(int(inp) == 2):
            item = obj_Q.dequeue()
            print("Item dequeued : " + str(item))
        elif(int(inp)==3):
            if obj_Q.isEmpty():
                print("Queue is empty")
            else:
                print("Queue not empty")
        elif(int(inp) == 4):
            print("Queue Size : ", obj_Q.size())    
        else:
            inp = input("Press 0: exit, 1: Enqueue, 2: Dequeue, 3: Is empty ?, 4: Queue size ? :")