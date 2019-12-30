import re
import random

class Favorization:

    def __init__(self, decision=0, whichElem=0, testObject=0):
        self.decision = ""
        self.whichElem = 0
        self.testObject=""

    def setDecision(self, a):
        self.decision = a

    def setWhichElem(self, a):
        self.whichElem = a

    def setTestObject(self, a):
        self.testObject = a

    def getDecision(self):
        return self.decision

    def getWhichElem(self):
        return self.whichElem

    def getTestObject(self):
        return self.testObject

class Decision:

    def __init__(self, decision=0, indexList=0):
        self.decision = ""
        self.indexList = []

    def setDecision(self, a):
        self.decision = a

    def setIndexList(self, a):
        self.indexList = a

    def getDecision(self):
        return self.decision

    def getIndexList(self):
        return self.indexList

class Classification:

    def __init__(self, decision=0, indexList=0):
        self.cObject = ""
        self.listOfClassifiedCorrectly = 0
        self.listOfClassified = 0

    def setCObject(self, a):
        self.cObject = a

    def setListOfClassifiedCorrectly(self, a):
        self.listOfClassifiedCorrectly = a

    def setListOfClassified(self, a):
        self.listOfClassified = a

    def getCObject(self):
        return self.cObject

    def getListOfClassifiedCorrectly(self):
        return self.listOfClassifiedCorrectly

    def getListOfClassified(self):
        return self.listOfClassified

class Param:

    def __init__(self, testObject=0, cObjet=0, param=0):
            self.testObject = ""  # x1,x2 etc.
            self.cObjet = ""  # c=1, c=0
            self.param = 0  # result

    def setTestObject(self, a):
            self.testObject = a

    def setCObjet(self, a):
            self.cObjet = a

    def setParam(self, a):
            self.param = a

    def getTestObject(self):
            return self.testObject

    def getCObject(self):
            return self.cObjet

    def getParam(self):
            return self.param

def listAttributesAndTheirNumbers(self):
    lines = splitIntoLines(self)
    myArray = []
    for line in lines:
        myArray.append(line.split(" "))
    return myArray

def printFile(self):
    f = open(self)
    print(f.read())

def splitIntoLines(self):
    return re.split(r'\n', self)

def delLastColumnAndRow(self):
    for i in range(len(self)):
        del self[i][len(self[i]) - 1]
    del self[len(self) - 1]
    return self

def getDecisions(array):
    result = []
    for i in range(len(array)):
        if not array[i][len(array[i]) - 1] in result:
            result.append(array[i][len(array[i]) - 1])
    return result

def getIndexOfDecision(array):
    decisions = getDecisions(array)
    result = []
    for x in decisions:
        decisionObject = Decision()
        decisionObject.setDecision(x)
        list = []
        for i in range(len(array)):
            if array[i][len(array[i]) - 1] == x:
                list.append(i)
        decisionObject.setIndexList(list)
        result.append(decisionObject)
    return result

class NaiwnyKlasyfikatorBayesa():
    def main(self):
        fDec = open("result/dec_bayes.txt", "w+")
        lines = listAttributesAndTheirNumbers(open("australian_TST.txt").read())
        australianTRN =listAttributesAndTheirNumbers(open("australian_TRN.txt").read())
        lines = delLastColumnAndRow(lines)
        australianTRN = delLastColumnAndRow(australianTRN)
        getTrnDecisions = getIndexOfDecision(australianTRN)

if __name__ == "__main__":
    NaiwnyKlasyfikatorBayesa.main("args")