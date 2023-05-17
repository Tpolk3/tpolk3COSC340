class direction:
    def __init__(self, p1, transition, p2, p2print):
        self.p1 = p1
        self.transition = transition
        self.p2 = p2
        self.p2print = p2print

    def getP1(self):
        return self.p1

    def getTransistion(self):
        return self.transition
    
    def getP2(self):
        return self.p2
    
    def getP2print(self):
        return self.p2print
    
    def __str__(self):
        return "(" + self.p1 + "," + self.readString + "," + self.wrightString + "," + self.p2 + "," + self.tapeDir + ")"

class mm:
    def __init__(self, inputList):
        stateStr = inputList[0]
        stateStr = stateStr.strip("\n")
        self.states = stateStr.split(",")
        self.startState = inputList[3].strip("\n")
        self.directions = inputList[4:]
        counter = 0
        while(counter < len(self.directions)):
            tempList = inputList[counter+4].split(",")
            tempList[len(tempList)-1] = tempList[len(tempList)-1].strip("\n")
            self.directions[counter] = direction(tempList[0], tempList[1], tempList[2], tempList[3])
            counter = counter + 1


    def runWith(self, inputString):
        startStateList = self.startState.split(",")
        retString = startStateList[1]
        currentState = startStateList[0]
        for x in inputString:
            transistion = False
            for y in self.directions:
                if not(transistion):
                    if currentState == y.getP1():
                        if x == y.getTransistion():
                            retString = retString + y.getP2print()
                            currentState = y.getP2()
                            transistion = True                   
        return retString




    
class inputReader():
    def __init__(self, fileName):
        self.fileName = fileName
    
    def readInFile(self):
        scanner = open(self.fileName, 'r')
        self.contents = scanner.readlines()
        scanner.close()

    
    def getContents(self):
        return self.contents


def runMM(mmText, inputText, outputText):
    iR1 = inputReader(mmText)
    iR2 = inputReader(inputText)
    iR1.readInFile()
    iR2.readInFile()
    mmParameters = iR1.getContents()
    mmInput = iR2.getContents()
    mm1 = mm(mmParameters)
    outPutFile = open(outputText, 'w')
    for x in mmInput:
        outcome = mm1.runWith(x.strip("\n"))
        outPutFile.write(outcome + "\n")
    outPutFile.close()

def main():
    mmText = 'mm.txt'
    inputText = 'input.txt'
    outputText = 'output.txt'
    runMM(mmText, inputText, outputText)
    
if(__name__ == "__main__"):
    main()