class TreasureChest():
    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points = points

    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self, answer):
        if self.__answer == answer:
            return True
        else: return False
    
    def getPoints(self, attempts):
        if attempts == 1: return self.__points
        elif attempts == 2: return self.__points // 2
        elif attempts == 3 or attempts == 4: return self.__points // 4
        else: return 0

def readData():
    global arrayTreasure

    try:
        with open('./TreasureChestData.txt', 'tr') as file:
            lines = 0
            # Read the amount of lines in file
            for line in file:
                lines += 1
            # Reset back to 0
            file.seek(0)
            lines = lines // 3
            
            arrayTreasure = []
            for i in range(lines):
                q = file.readline().strip('\n')
                a = int(file.readline().strip('\n'))
                p = int(file.readline().strip('\n'))
                arrayTreasure.append(TreasureChest(q, a, p))

    except:
        raise FileNotFoundError('The file is not available!!1!1!')

# Main
readData()
attempts = 1
qNum = int(input('Enter a value between 1 and 5: '))
qNum -= 1

print(arrayTreasure[qNum].getQuestion())
while arrayTreasure[qNum].checkAnswer(int(input('Enter your answer:'))) != True:
    attempts += 1

print(attempts)
print(arrayTreasure[qNum].getPoints(attempts))