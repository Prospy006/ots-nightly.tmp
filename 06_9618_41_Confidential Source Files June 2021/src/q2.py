def linearSearch(search: int):
    found = False
    for i in range(len(arrayData)):
        if arrayData[i] == search:
            found = True
        i += 1
    
    if found == True: return True
    else: return False

def bubbleSort(theArray):
    temp: int = 0
    arrayLen = len(theArray)

    for x in range(0, arrayLen):
        insideLen = arrayLen - 1

        for y in range(0, insideLen):
            if theArray[y] < theArray[y + 1]:
                temp = theArray[y]
                theArray[y] = theArray[y + 1]
                theArray[y + 1] = temp


# Main
arrayData = [int for i in range(10)]
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

if linearSearch(int(input('Input a value to search for: '))) == True: print('Value was found')
else: print('Value was not found')

print(arrayData)
bubbleSort(arrayData)
print(arrayData)