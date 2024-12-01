import re

def assignemt1():
    file = open('day 1/file.txt', 'r')
    lines = [line.strip() for line in file]
    result = 0
    list1, list2 = getList(lines)
    list1sorted = sorted(list1)
    list2sorted = sorted(list2)
    for i in range(len(list1sorted)):
        result += abs(list1sorted[i] - list2sorted[i])
    return(result)

def assignemt2():
    file = open('day 1/file.txt', 'r')
    lines = [line.strip() for line in file]
    list1, list2 = getList(lines)
    result = processScore(list1,list2)
    return(result)

def processScore(list1, list2):
    result = 0
    for num1 in list1:
        count = 0
        for num2 in list2:
            if num1 == num2:
                count += 1
        result += num1 * count
    return(result)

def getList(lines):
    list1 = []
    list2 = []
    for line in lines:
        line = line.split(' ')
        list1.append(int(line[0]))
        list2.append(int(line[-1]))
    return list1, list2

print(assignemt2())