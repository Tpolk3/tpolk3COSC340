import sys

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
    
class Node:
    def __init__(self, id):
        self.id = id
        self.dList = []

    #must alread have a list of nodes that you wish to point to in the enviorment that you create this node to set a pointer
    def setPointers(self, dirList, nodeList):
        for d in dirList:
            for node in nodeList:
                if(node.getID() == d.getP2()):
                 self.dList.append((d.getTransistion(), node))

    def getDest(self, x):
        retList = []
        for d in self.dList:
            if(d[0] == x):
                retList.append(d[1])
        return retList
    
    def getID(self):
        return self.id
    
    def __str__(self):
        return self.id




class nfa:
    def __init__(self, inputList):
        self.nodeList = []
        self.finalStates = []
        stateStr = inputList[0]
        stateStr = stateStr.strip("\n")
        stateStr = stateStr.split(",")
        for s in stateStr:
            self.nodeList.append(Node(s))

        startStateStr = inputList[2].strip("\n")
        finalStatesStr = inputList[3].strip("\n")
        finalStatesStr = finalStatesStr.split(",")
        directions = inputList[4:]
        counter = 0
        while(counter < len(directions)):
            tempList = inputList[counter+4].split(",")
            tempList[2] = tempList[2].strip("\n")
            directions[counter] = direction(tempList[0], tempList[1], tempList[2])
            counter = counter + 1
        
        for n in self.nodeList:
            if(startStateStr == n.getID()):
                self.startState = n
            for x in finalStatesStr:
                if(x == n.getID()):
                    self.finalStates.append(n)

        for n in self.nodeList:
            tempList = []
            for d in directions:
                if(d.getP1() == n.getID()):
                    tempList.append(d)
                n.setPointers(tempList, self.nodeList)
        

    def runWith(self, inputString):
        if(inputString == "@"):
            inputString = ""
        def fn(self, n, s):
            try:
                de = n.getDest("@")
                for x in de:
                    b = fn(self, x, s)
                    if(b == True):
                        return True
            except:
                return True
            if(s == ""):
                for x in self.finalStates:
                    if(n == x):
                        return True
                return False
            de = n.getDest(s[0])
            for x in de:
                b = fn(self, x, s[1:])
                if(b == True):
                    return True
            return False
        return fn(self, self.startState, inputString)


    
class inputReader():
    def __init__(self, fileName):
        self.fileName = fileName
    
    def readInFile(self):
        scanner = open(self.fileName)
        self.contents = scanner.readlines()
        scanner.close()

    
    def getContents(self):
        return self.contents


def runnfaMachine(nfaText, inputText, outputText):
    iR1 = inputReader(nfaText)
    iR2 = inputReader(inputText)
    iR1.readInFile()
    iR2.readInFile()
    nfaParameters = iR1.getContents()
    nfaInput = iR2.getContents()
    nfa1 = nfa(nfaParameters)
    outPutFile = open(outputText, 'w')
    count = 1
    for x in nfaInput:
        outcome = nfa1.runWith(x.strip("\n"))
        if outcome:
            outPutFile.write("accept\n")
            count = count + 1
        else:
            outPutFile.write("reject\n")
            count = count + 1
    outPutFile.close()

def main():
    #Testing
    nfaText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 3/example3/nfa.txt"
    inputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 3/input.txt"
    outputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 3/outputTest.txt"
    runnfaMachine(nfaText, inputText, outputText)

    
    #Example1
    nfaText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 3/example1/nfa.txt"
    inputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 3/example1/input.txt"
    outputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 3/example1/outputTest.txt"
    runnfaMachine(nfaText, inputText, outputText)

    #Example2
    nfaText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 3/example2/nfa.txt"
    inputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 3/example2/input.txt"
    outputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 3/example2/outputTest.txt"
    runnfaMachine(nfaText, inputText, outputText)

    #Example3
    nfaText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 3/example3/nfa.txt"
    inputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 3/example3/input.txt"
    outputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 3/example3/outputTest.txt"
    runnfaMachine(nfaText, inputText, outputText)

    #Example4
    nfaText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 3/example4/nfa.txt"
    inputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 3/example4/input.txt"
    outputText = "/Users/tylerpolk/Github Classwork/tpolk3COSC340/Project 3/example4/outputTest.txt"
    runnfaMachine(nfaText, inputText, outputText)
    
    
    
if(__name__ == "__main__"):
    main()