
def assignemt1():
    file = open('day 7/file.txt', 'r')
    lines = [line.strip() for line in file]
    result = 0
    for i in range(len(lines)):
        (checkResult, numbers) = getData(lines[i])
        combinations = findCombinations(numbers)
    return checkResult


def findCombinations(numbers):
    operators = ['+', '*']



def checkCalibrations(result,numbers):
    pass

def getData(line):
    split = line.split(':')
    check = int(split[0])
    string = split[1].strip()
    numbers = string.split(' ')
    numbers = [int(n) for n in numbers]
    return (check, numbers)

assignemt1()