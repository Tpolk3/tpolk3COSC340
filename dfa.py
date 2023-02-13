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

class dfa:
    def __init__(self, inputList):
        self.states = inputList[0]
        self.alphabet = inputList[1]
        self.startStates = inputList[2]
        self.finalStates = inputList[3]
        self.transistionRules = inputList[4]
    
class inputReader():
    def __init__(self, fileName):
        self.fileName = fileName

def main():
    inputReader()
    
if(__name__ == "__main__"):
    main()