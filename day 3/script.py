import re
def assignemt1():
    file = open('day 3/file.txt', 'r')
    lines = [line.strip() for line in file]
    result = 0
    for line in lines:
        mullList = re.findall(r"mul\((\d+),(\d+)\)", line)
        for list in mullList:
            result += int(list[0]) * int(list[-1])
    return result

assignemt1()