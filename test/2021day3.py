from enum import Enum
file = open('test/file2021-3.txt', 'r')
lines = [line.strip() for line in file]

def assignemt1():
    lengthOfString = len(lines[0])
    epsilon = ''
    gamma = ''
    for i in range(lengthOfString):
        numberOfZeros = 0
        numberOfOnes = 0
        for line in lines:
            if line[i] == '0':
                numberOfZeros += 1
            else:
                numberOfOnes += 1
        if numberOfOnes > numberOfZeros:
            gamma += '0'
            epsilon += '1'
        else:
            epsilon += '0'
            gamma += '1'
    return(int(gamma,2) * int(epsilon,2))


def assignemt2():
    oxygen = loopThrouhLines(Type.OXYGEN)
    co2Scrubber = loopThrouhLines(Type.CO2SCRUBBER)
    return(int(oxygen,2) * int(co2Scrubber,2))
    

def loopThrouhLines(type):
    lengthOfString = len(lines[0])
    linesToGoThrough = lines
    for i in range(lengthOfString):
        numberOfZeros = 0
        numberOfOnes = 0
        for line in linesToGoThrough:
            if line[i] == '0':
                numberOfZeros += 1
            else:
                numberOfOnes += 1
        keepValue = getValue(numberOfZeros,numberOfOnes,type)
        linesToGoThrough = createNewLines(i,keepValue,linesToGoThrough)
        if len(linesToGoThrough) == 1:
            return(linesToGoThrough[0])
    return(0)

def getValue(numberOfZeros,numberOfOnes,type):
        if numberOfOnes > numberOfZeros:
            if type == Type.OXYGEN:
                keepValue = '1'
            else:
                keepValue = '0'
        elif numberOfOnes < numberOfZeros:
            if type == Type.OXYGEN:
                keepValue = '0'
            else:
                keepValue = '1'
        else:
            if type == Type.OXYGEN:
                keepValue = '1'
            else:
                keepValue = '0'
        return(keepValue)


def createNewLines(index,value,liness):
    newLines = []
    for line in liness:
        if line[index] == value:
            newLines.append(line)
    return(newLines)



class Type(Enum):
    OXYGEN = 1
    CO2SCRUBBER = 2

print(assignemt2())