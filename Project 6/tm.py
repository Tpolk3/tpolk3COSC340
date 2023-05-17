from time import sleep

class direction:
    def __init__(self, p1, readString, wrightString, p2, tapeDir):
        self.p1 = p1
        self.readString = readString
        self.wrightString = wrightString
        self.p2 = p2
        self.tapeDir = tapeDir

    def getP1(self):
        return self.p1

    def getReadString(self):
        return self.readString

    def getWrightString(self):
        return self.wrightString
    
    def getP2(self):
        return self.p2
    
    def getTapeDir(self):
        return self.tapeDir
    
    def __str__(self):
        return "(" + self.p1 + "," + self.readString + "," + self.wrightString + "," + self.p2 + "," + self.tapeDir + ")"

class tm:
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
            self.directions[counter] = direction(tempList[0], tempList[1], tempList[2], tempList[3], tempList[4])
            counter = counter + 1


    def runWith(self, inputString):
        tape = []
        tape[:0] = inputString
        tapeHead = 0
        currentState = self.startState
        counter = 0
        while(True):
            found = False
            for x in self.directions:
                if(not(found)):
                    if(x.getP1() == currentState):
                        if(x.getReadString() == tape[tapeHead]):
                            found = True
                            tape[tapeHead] = x.getWrightString()
                            currentState = x.getP2()
                            if(x.getTapeDir() == "R"):
                                tapeHead = tapeHead+1
                                if(tapeHead> len(tape)-1):
                                    tape.append("_")
                            if(x.getTapeDir() == "L"):
                                if(tapeHead < 0):
                                    tape.insert(0, "_")
                                    tapeHead = tapeHead+1
                                tapeHead = tapeHead-1
                            if(currentState == "accept"):
                                return True
                            if(currentState == "reject"):
                                return False
            if(found == False):
                return False



    
class inputReader():
    def __init__(self, fileName):
        self.fileName = fileName
    
    def readInFile(self):
        scanner = open(self.fileName, 'r')
        self.contents = scanner.readlines()
        scanner.close()

    
    def getContents(self):
        return self.contents


def runTM(tmText, inputText, outputText):
    iR1 = inputReader(tmText)
    iR2 = inputReader(inputText)
    iR1.readInFile()
    iR2.readInFile()
    tmParameters = iR1.getContents()
    tmInput = iR2.getContents()
    tm1 = tm(tmParameters)
    outPutFile = open(outputText, 'w')
    for x in tmInput:
        outcome = tm1.runWith(x.strip("\n"))
        if outcome:
            outPutFile.write("accept\n")
        else:
            outPutFile.write("reject\n")
    outPutFile.close()

def main():
    #Testing
    """
    tmText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 5/example1/tm.txt"
    inputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 5/input.txt"
    outputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 5/outputTest.txt"
    """
    #runTM(tmText, inputText, outputText)

    tmText = 'tm.txt'
    inputText = 'input.txt'
    outputText = 'output.txt'
    runTM(tmText, inputText, outputText)
    
   

    
if(__name__ == "__main__"):
    main()