from collections import deque

class direction:
    def __init__(self, p1, readString, popString, p2, pushString):
        self.p1 = p1
        self.readString = readString
        self.popString = popString
        self.p2 = p2
        self.pushString = pushString

    def getP1(self):
        return self.p1

    def getReadString(self):
        return self.readString

    def getPopString(self):
        return self.popString
    
    def getP2(self):
        return self.p2
    
    def getPushString(self):
        return self.pushString
    
    def __str__(self):
        return "(" + self.p1 + "," + self.readString + "," + self.popString + "," + self.p2 + "," + self.pushString + ")"

class dpda:
    def __init__(self, inputList):
        #TODO
        stateStr = inputList[0]
        stateStr = stateStr.strip("\n")
        self.states = stateStr.split(",")
        self.startState = inputList[3].strip("\n")
        finalStatesStr = inputList[4].strip("\n")
        self.finalStates = finalStatesStr.split(",")
        self.directions = inputList[5:]
        counter = 0
        while(counter < len(self.directions)):
            tempList = inputList[counter+5].split(",")
            tempList[len(tempList)-1] = tempList[len(tempList)-1].strip("\n")
            self.directions[counter] = direction(tempList[0], tempList[1], tempList[2], tempList[3], tempList[4])
            counter = counter + 1


    def runWith(self, inputString):
        currentState = self.startState
        bottomOfStackVar = ""
        stack = deque()
        for d in self.directions:
            if(self.startState == (d.getP1())):
                stack.append(d.getPushString())
                bottomOfStackVar = d.getPushString()
                currentState = d.getP2()

        for x in inputString:
            transition = False
            for d in self.directions:
                if(not(transition)):
                    if(currentState == (d.getP1())):
                        if(x == (d.getReadString())):
                            topOfStackVar = stack.pop()
                            if(d.getPopString() == ("@")):
                                transition = True
                                stack.append(topOfStackVar)
                                if(not(d.getPushString() == ("@"))):
                                    stack.append(d.getPushString())
                                currentState = d.getP2()
                            elif(d.getPopString() == (topOfStackVar)):
                                transition = True
                                if(not(d.getPushString() == ("@"))):
                                    stack.append(d.getPushString())
                                currentState = d.getP2()
                            else:
                                stack.append(topOfStackVar)
            if(not(transition)):
                return False

        try:
            checkforBottomVar = stack.pop()
        except:
            return False
        for d in self.directions:
            if(currentState == (d.getP1())):
                if(d.getPopString() == (bottomOfStackVar)):
                    if(checkforBottomVar == (bottomOfStackVar)):
                        currentState = d.getP2()

        for s in self.finalStates:
            if(s == (currentState)):
                return True
        
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


def runDPDAMachine(dpdaText, inputText, outputText):
    iR1 = inputReader(dpdaText)
    iR2 = inputReader(inputText)
    iR1.readInFile()
    iR2.readInFile()
    dpdaParameters = iR1.getContents()
    dpdaInput = iR2.getContents()
    dpda1 = dpda(dpdaParameters)
    outPutFile = open(outputText, 'w')
    for x in dpdaInput:
        outcome = dpda1.runWith(x.strip("\n"))
        if outcome:
            outPutFile.write("accept\n")
        else:
            outPutFile.write("reject\n")
    outPutFile.close()

def main():
    #Testing
    """
    dpdaText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 5/example1/dpda.txt"
    inputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 5/input.txt"
    outputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 5/outputTest.txt"
    """
    #runDPDAMachine(dpdaText, inputText, outputText)

    dpdaText = 'dpda.txt'
    inputText = 'input.txt'
    outputText = 'output.txt'
    runDPDAMachine(dpdaText, inputText, outputText)
    
    """
    #Example1
    dpdaText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 5/example1/dpda.txt"
    inputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 5/example1/input.txt"
    outputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 5/example1/outputTest.txt"
    runDPDAMachine(dpdaText, inputText, outputText)

    #Example2
    dpdaText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 5/example2/dpda.txt"
    inputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 5/example2/input.txt"
    outputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 5/example2/outputTest.txt"
    runDPDAMachine(dpdaText, inputText, outputText)
    """

    
if(__name__ == "__main__"):
    main()