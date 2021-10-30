# The main code to test the methods of Deque functionality


import lineards

if __name__ == '__main__':
    obj_Deq = lineards.Deque()
    
    while True:
        inp = input("Press 0: exit, 1: Add front, 2: Add Rear, 3: Remove Front, 4: Remove Rear, 5:Is empty ?, 6: Queue size ? : ")

        if(int(inp) == 0):
            break
        elif(int(inp) == 1):
            num = input("Enter no to Add to Front : ")
            obj_Deq.addFront(int(num))
        elif(int(inp) == 2):
            num = input("Enter no to Add to Rear : ")
            obj_Deq.addRear(int(num))
        elif(int(inp)== 3):
            item_rem = obj_Deq.removeFront()
            print("Item Removed from front : " + str(item_rem))
        elif(int(inp)== 4):    
            item_rem = obj_Deq.removeRear()
            print("Item Removed from rear : " + str(item_rem))
        elif(int(inp)== 5):
            if obj_Deq.isEmpty():
                print("Queue is empty")
            else:
                print("Queue not empty")
        elif(int(inp) == 6):
            print("Queue Size : ", obj_Deq.size())    
        else:
            print("Press 0: exit, 1: Add front, 2: Add Rear, 3: Remove Front, 4: Remove Rear, 5:Is empty ?, 6: Queue size ? : ")