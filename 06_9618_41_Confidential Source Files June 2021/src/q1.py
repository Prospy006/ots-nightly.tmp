# Class node:
class Node:
    def __init__(self, data, nextNode: int):
        self.data = data
        self.nextNode = nextNode

def outputNodes(linkedList, startPointer: int):
    while linkedList[startPointer].nextNode != -1:
        print(linkedList[startPointer].data)
        startPointer = linkedList[startPointer].nextNode

    if linkedList[startPointer].nextNode == -1:
        return linkedList[startPointer].data


def addNode(linkedList: list, startPointer: int, emptyList: int):
    data = int(input('Input the data to be stored: '))
    currentPointer = startPointer

    # If no nodes in linkedlist;
    if startPointer == -1:
        linkedList[0] = Node(data, 1)
        startPointer = 0
        emptyList = 1
        return True

    # Return if no free spaces
    if emptyList == -1 or linkedList[emptyList].data != 0:
        return False
    
    # Find next free space
    while linkedList[currentPointer].data != 0:
        currentPointer += 1

    if linkedList[currentPointer].data == 0:
        emptyList = currentPointer + 1

        while linkedList[emptyList].data != 0:
            emptyList += 1

        linkedList[currentPointer] = Node(data, emptyList)
        return True
    
# Declarations: 
startPointer = 0
emptyList = 5
linkedList = [Node for i in range(10)]

# Inputting nodes:
linkedList[0] = Node(1, 1)
linkedList[1] = Node(5, 4)
linkedList[2] = Node(6, 7)
linkedList[3] = Node(7, -1)
linkedList[4] = Node(2, 2)
linkedList[5] = Node(0, 6)
linkedList[6] = Node(0, 8)
linkedList[7] = Node(56, 3)
linkedList[8] = Node(0, 9)
linkedList[9] = Node(0, -1)

# Main
outputNodes(linkedList, startPointer)

result = addNode(linkedList, startPointer, emptyList)
if result == True:
    print('Node added to the linkedList.')
else:
    print('Node was not added LLLLLLLLLLLLLL')

outputNodes(linkedList, startPointer)