import itertools

def assignemt1():
    file = open('day 7/file.txt', 'r')
    lines = [line.strip() for line in file]
    result = 0
    for i in range(len(lines)):
        (checkResult, numbers) = getData(lines[i])
        combinations = findCombinations(numbers)
        if checkCalibration(checkResult,numbers,combinations):
            result += checkResult
    return result


def checkCalibration(result,numbers,combinations):
    for combination in combinations:
        num = numbers[0]
        for i in range(1,len(numbers),1):
            if combination[i-1] == '+':
                num += numbers[i]
            elif combination[i-1] == '*':
                num *= numbers[i]
        if num == result:
            return True
    return False


def findCombinations(numbers):
    operators = ['+', '*']
    return list(itertools.product(operators, repeat=len(numbers)-1))

def getData(line):
    split = line.split(':')
    check = int(split[0])
    string = split[1].strip()
    numbers = string.split(' ')
    numbers = [int(n) for n in numbers]
    return (check, numbers)

print(assignemt1())