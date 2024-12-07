
def assignemt1():
    file = open('day 6/file.txt', 'r')
    lines = [line.strip() for line in file]
    twoDArr = createTwoDArr(lines)
    currentPosition = findStartPosition(twoDArr)
    currentDirectionIndex = 0
    while True:
        twoDArr = markArr(twoDArr,currentPosition,'X')
        nextPosition = findNextPosition(currentPosition,currentDirectionIndex)
        if checkIndexOutOfBounds(twoDArr,nextPosition):
            break
        Symbol = findNextSymboID(nextPosition,twoDArr)
        if symbolIsWall(Symbol):
            currentDirectionIndex = updateDirectionIndex(currentDirectionIndex)
        else:
            currentPosition = nextPosition
    return findResult(twoDArr)



def assignemt2():
    file = open('day 6/file.txt', 'r')
    lines = [line.strip() for line in file]
    twoDArr = createTwoDArr(lines)
    currentPosition = findStartPosition(twoDArr)
    currentDirectionIndex = 0
    obstructions = []
    justMoved = False
    while True:
        nextPosition = findNextPosition(currentPosition,currentDirectionIndex)
        if checkForInfinityLoop(twoDArr,currentPosition,currentDirectionIndex,justMoved):
            obstructions.append(nextPosition)
        if checkIndexOutOfBounds(twoDArr,nextPosition):
            break
        symbol = findNextSymboID(nextPosition,twoDArr)
        if symbolIsWall(symbol):
            justMoved = True
            currentDirectionIndex = updateDirectionIndex(currentDirectionIndex)
        else:
            justMoved = False
            currentPosition = nextPosition
        twoDArr = markpart2(twoDArr,currentPosition,currentDirectionIndex)
    return len(obstructions)

def checkForInfinityLoop(twoDArr,position,index,moved):
    if moved:
        return False
    (y,x) = position
    if index == 0:
        return checkLine(1,0,x,y,'-',twoDArr)
    if index == 1:
        return checkLine(0,1,x,y,'|',twoDArr)
    if index == 2:
        return checkLine(-1,0,x,y,'-',twoDArr)
    if index == 3:
        return checkLine(0,-1,x,y,'|',twoDArr)
    
def checkLine(xIncr,yIncr,x,y,check,twoDArr):
    wallFound = False
    valueFound = False
    while True:
        x += xIncr
        y += yIncr
        if y < 0 or x < 0:
            break
        try: value = twoDArr[y][x]
        except IndexError: 
            break
        if value == '+' or value == check:
            valueFound = True
        if value == '#':
            wallFound = True
    return valueFound and wallFound


def markpart2(twoDArr,position,index):
    (y,x) = position
    symbol = None
    if twoDArr[y][x] == '^':
        return twoDArr
    if index == 0 or index == 2:
        symbol = '|'
    if index == 1 or index == 3:
        symbol = '-'
    if twoDArr[y][x] == '|' or twoDArr[y][x] == '-':
        symbol = '+'
    twoDArr[y][x] = symbol
    return twoDArr

def findResult(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'X':
                result += 1
    return result

def markArr(twoDArr,position,mark):
    (y,x) = position
    twoDArr[y][x] = mark
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


print(f'Assignemt 1: {assignemt1()}')
print(f'Assignemt 2: {assignemt2()}')