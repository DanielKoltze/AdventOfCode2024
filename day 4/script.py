import re
def assignemt1():
    file = open('day 4/file.txt', 'r')
    matrix = [line.strip() for line in file]
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result += checkForWord((i,j),[(0,1),(0,2),(0,3)], matrix)
            result += checkForWord((i,j),[(0,-1),(0,-2),(0,-3)], matrix)
            result += checkForWord((i,j),[(1,0),(2,0),(3,0)], matrix)
            result += checkForWord((i,j),[(-1,0),(-2,0),(-3,0)], matrix)
            result += checkForWord((i,j),[(1,1),(2,2),(3,3)], matrix)
            result += checkForWord((i,j),[(-1,-1),(-2,-2),(-3,-3)], matrix)
            result += checkForWord((i,j),[(-1,1),(-2,2),(-3,3)], matrix)
            result += checkForWord((i,j),[(1,-1),(2,-2),(3,-3)], matrix)

    return result
def checkForWord(currentPosition, positionsToCheck, matrix):
    WORD = 'XMAS'
    currentY,currentX = currentPosition
    positionsToCheck.insert(0,(0,0))
    for i, tuple in enumerate(positionsToCheck, start=0):
        addY,addX = tuple
        y = currentY + addY
        x = currentX + addX
        if x < 0 or y < 0:
            return 0
        
        try: value = matrix[y][x]
        except IndexError: return 0
        
        if value != WORD[i]:
            return 0
    return 1

print(assignemt1())