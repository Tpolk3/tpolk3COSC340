class direction:
    def __init__(self, p1, transistion, p2):
        self.p1 = p1
        self.transistion = transistion
        self.p2 = p2

    def getP1(self):
        return self.p1

    def getTransistion(self):
        return self.transistion

    def getP2(self):
        return self.p2
    
    def __str__(self):
        return "(" + self.p1 + "," + self.transistion + "," + self.p2 + ")" #+"\n"

class dfa:
    def __init__(self, inputList):
        self.states = inputList[0]
        self.alphabet = inputList[1]
        self.startState = inputList[2]
        self.finalStates = inputList[3]
        self.directions = inputList[4:]
        counter = 0
        while(counter < len(self.directions)):
            self.directions[counter] = direction(inputList[counter+4][0:2], inputList[counter+4][3:4], inputList[counter+4][5:7])
            counter = counter + 1

    def runWith(self, inputString):
        currentState = self.startState[0:2]
        for x in inputString:
            for y in self.directions:
                if currentState == y.getP1():
                    if x == y.getTransistion():
                        currentState = y.getP2()
                        break
        counter = 0
        while(counter < len(self.finalStates)-2):
            if currentState == self.finalStates[counter:counter+2]:
                return True
            counter = counter + 3
        return False

    
class inputReader():
    def __init__(self, fileName):
        self.fileName = fileName
    
    def readInFile(self):
        scanner = open(self.fileName)
        self.contents = scanner.readlines()
        scanner.close()

    
    def getContents(self):
        return self.contents


def runDFAMachine(dfaText, inputText, outputText):
    iR1 = inputReader(dfaText)
    iR2 = inputReader(inputText)
    iR1.readInFile()
    iR2.readInFile()
    dfaParameters = iR1.getContents()
    dfaInput = iR2.getContents()
    dfa1 = dfa(dfaParameters)
    outPutFile = open(outputText, 'w')
    for x in dfaInput:
        outcome = dfa1.runWith(x)
        if outcome:
            outPutFile.write("accept\n")
        else:
            outPutFile.write("reject\n")
    outPutFile.close()

def main():
    dfaText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Cosc 340 Project 1/example1/dfa.txt"
    inputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Cosc 340 Project 1/example1/input.txt"
    outputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Cosc 340 Project 1/example1/outputTest1.txt"
    runDFAMachine(dfaText, inputText, outputText)

    
if(__name__ == "__main__"):
    main()