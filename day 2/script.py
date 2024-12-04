
def assignemt1():
    file = open('day 2/file.txt', 'r')
    lines = [line.strip() for line in file]
    result = 0
    for line in lines:
        numbers = line.split(' ')
        if CheckCurrentReport(numbers):
            result += 1
    return result

def assignemt2():
    file = open('day 2/file.txt', 'r')
    lines = [line.strip() for line in file]
    result = 0
    for line in lines:
        numbers = line.split(' ')
        for i in range(len(numbers)):
            checkNumbers = numbers[:]
            del checkNumbers[i]
            if CheckCurrentReport(checkNumbers):
                result += 1
                break
    return result

def CheckCurrentReport(numbers):
    for i in range(len(numbers)):
        currentNum = int(numbers[i])
        if i == 0:
            nextNum = int(numbers[i+1])
            if nextNum > currentNum:
                isIncresing = True
            elif nextNum == currentNum:
                return
            else:
                isIncresing = False
        else:
            previousNum = int(numbers[i-1])
            if isIncresing and currentNum != previousNum and currentNum > previousNum and currentNum < previousNum + 4:
                pass
            elif not isIncresing and currentNum != previousNum and currentNum < previousNum and currentNum > previousNum - 4:
                pass
            else:
                return False
    return True


print(assignemt2())
