import re
def assignemt1():
    file = open('day 4/file.txt', 'r')
    matrix = [line.strip() for line in file]
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result += checkForWord((i,j),[(0,0),(0,1),(0,2),(0,3)], matrix,'XMAS')
            result += checkForWord((i,j),[(0,0),(0,-1),(0,-2),(0,-3)], matrix,'XMAS')
            result += checkForWord((i,j),[(0,0),(1,0),(2,0),(3,0)], matrix,'XMAS')
            result += checkForWord((i,j),[(0,0),(-1,0),(-2,0),(-3,0)], matrix,'XMAS')
            result += checkForWord((i,j),[(0,0),(1,1),(2,2),(3,3)], matrix,'XMAS')
            result += checkForWord((i,j),[(0,0),(-1,-1),(-2,-2),(-3,-3)], matrix,'XMAS')
            result += checkForWord((i,j),[(0,0),(-1,1),(-2,2),(-3,3)], matrix,'XMAS')
            result += checkForWord((i,j),[(0,0),(1,-1),(2,-2),(3,-3)], matrix,'XMAS')
    return result

def checkForWord(currentPosition, positionsToCheck, matrix, WORD):
    currentY,currentX = currentPosition
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


def assignemt2():
    file = open('day 4/file.txt', 'r')
    matrix = [line.strip() for line in file]
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            check = 0
            check += checkForWord((i,j),[(-1,-1),(0,0),(1,1)], matrix,'MAS')
            check += checkForWord((i,j),[(-1,-1),(0,0),(1,1)], matrix,'SAM')
            check += checkForWord((i,j),[(1,-1),(0,0),(-1,1)], matrix,'MAS')
            check += checkForWord((i,j),[(1,-1),(0,0),(-1,1)], matrix,'SAM')
            if check == 2:
                result += 1
    return result

print(f'Assignment 1: {assignemt1()}')
print(f'Assignment 2: {assignemt2()}')