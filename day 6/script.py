
def assignemt1():
    file = open('day 6/file.txt', 'r')
    lines = [line.strip() for line in file]
    twoDArr = createTwoDArr(lines)
    currentPosition = findStartPosition(twoDArr)
    currentDirectionIndex = 0
    while True:
        twoDArr = markArr(twoDArr,currentPosition)
        nextPosition = findNextPosition(currentPosition,currentDirectionIndex)
        if checkIndexOutOfBounds(twoDArr,nextPosition):
            break
        Symbol = findNextSymboID(nextPosition,twoDArr)
        if symbolIsWall(Symbol):
            currentDirectionIndex = updateDirectionIndex(currentDirectionIndex)
        else:
            currentPosition = nextPosition
    return findResult(twoDArr)

def findResult(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'X':
                result += 1
    return result

def markArr(twoDArr,position):
    (y,x) = position
    twoDArr[y][x] = 'X'
    return twoDArr

def updateDirectionIndex(directionIndex):
    if directionIndex == 3:
        return 0
    return directionIndex + 1

def symbolIsWall(symbol):
    return symbol == '#'

def findNextSymboID(position,arr):
    (y,x) = position
    return arr[y][x]

def findNextPosition(position,directionIndex):
    y,x = position
    if directionIndex == 0:
        y -= 1
    if directionIndex == 2:
        y += 1
    if directionIndex == 1:
        x += 1
    if directionIndex == 3:
        x -= 1
    return (y,x)

def checkIndexOutOfBounds(twoDArr,position):
    (y,x) = position
    if y < 0 or x < 0:
        return True
    if len(twoDArr) <= y or len(twoDArr[0]) <= x:
        return True
    return False

def findStartPosition(twoDArr):
    for i in range(len(twoDArr)):
        for j in range(len(twoDArr[i])):
            if twoDArr[i][j] == '^':
                return (i,j)

def createTwoDArr(lines):
    arr = []
    for line in lines:
        innerArr = []
        for char in line:
            innerArr.append(char)
        arr.append(innerArr)
    return arr


print(assignemt1())