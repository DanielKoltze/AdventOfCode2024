file = open('test/file.txt', 'r')
lines = file.readlines()

def assignemt1():
    count = 0
    for i in range(1,len(lines)):
        value = int(lines[i])
        checkValue = int(lines[i-1])
        if checkIfValueIsHiger(value,checkValue):
            count += 1
    return(count)

def assignemt2():
    count = 0
    treeMeasurement = []
    for i in range(len(lines)-2):
        sum = sumList([lines[i],lines[i+1],lines[i+2]])
        treeMeasurement.append(sum)
    for i in range(1,len(treeMeasurement)):
        value = int(treeMeasurement[i])
        checkValue = int(treeMeasurement[i-1])
        if checkIfValueIsHiger(value,checkValue):
            count += 1
    return(count)


def sumList(list):
    sum = 0
    for number in list:
        sum += int(number)
    return sum

def checkIfValueIsHiger(value,checkvalue):
    if value > checkvalue:
        return True
    return False

print(assignemt2())