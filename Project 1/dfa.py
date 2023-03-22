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
        return "(" + self.p1 + "," + self.transistion + "," + self.p2 + ")"

class dfa:
    def __init__(self, inputList):
        self.startState = inputList[2].strip("\n")
        self.finalStates = inputList[3].split(",")
        self.directions = inputList[4:]
        counter = 0
        while(counter < len(self.directions)):
            tempList = inputList[counter+4].split(",")
            tempList[2] = tempList[2].strip("\n")
            self.directions[counter] = direction(tempList[0], tempList[1], tempList[2])
            counter = counter + 1

    def runWith(self, inputString):
        currentState = self.startState
        for x in inputString:
            transistion = False
            for y in self.directions:
                if not(transistion):
                    if currentState == y.getP1():
                        if x == y.getTransistion():
                            currentState = y.getP2()
                            transistion = True                   
        for x in self.finalStates:
            x = x.strip("\n")
            if currentState == x:
                return True
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
    #Testing
    dfaText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 1/example2/dfa.txt"
    inputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 1/input.txt"
    outputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 1/outputTest.txt"
    #runDFAMachine(dfaText, inputText, outputText)

    #Example1
    dfaText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 1/example1/dfa.txt"
    inputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 1/example1/input.txt"
    outputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 1/example1/outputTest.txt"
    runDFAMachine(dfaText, inputText, outputText)

    #Example2
    dfaText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 1/example2/dfa.txt"
    inputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 1/example2/input.txt"
    outputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 1/example2/outputTest.txt"
    runDFAMachine(dfaText, inputText, outputText)

    #Example3
    dfaText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 1/example3/dfa.txt"
    inputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 1/example3/input.txt"
    outputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 1/example3/outputTest.txt"
    runDFAMachine(dfaText, inputText, outputText)

    #Example4
    dfaText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 1/example4/dfa.txt"
    inputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 1/example4/input.txt"
    outputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 1/example4/outputTest.txt"
    runDFAMachine(dfaText, inputText, outputText)

    
if(__name__ == "__main__"):
    main()