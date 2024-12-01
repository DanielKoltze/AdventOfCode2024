file = open('test/file2021-2.txt', 'r')
lines = file.readlines()

def assignemt1():
    horizontal = 0
    depth = 0
    for line in lines:
        linevalue = line.split(' ')
        if linevalue[0] == 'forward':
            horizontal += int(linevalue[1])
        elif linevalue[0] == 'up':
            depth -= int(linevalue[1])
        elif linevalue[0] == 'down':
            depth += int(linevalue[1])
    return depth * horizontal

def assignemt2():
    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        linevalue = line.split(' ')
        if linevalue[0] == 'forward':
            horizontal += int(linevalue[1])
            depth += int(linevalue[1]) * aim
        elif linevalue[0] == 'up':
            aim -= int(linevalue[1])
        elif linevalue[0] == 'down':
            aim += int(linevalue[1])
    return depth * horizontal

print(assignemt2())