
def assignemt1():
    file = open('test/file2015-1.txt', 'r')
    lines = [line.strip() for line in file]
    wrappingPaperSize = 0
    for line in lines:
        sizes = line.split('x')
        l = int(sizes[0])
        w = int(sizes[1])
        h = int(sizes[2])
        wrappingPaperSize += 2*l*w + 2*w*h + 2*h*l + min([l*w,w*h,h*l])
    return(wrappingPaperSize)

def assignemt2():
    file = open('test/file2015-1.txt', 'r')
    lines = [line.strip() for line in file]
    wrappingPaperSize = 0
    for line in lines:
        sizes = line.split('x')
        l = int(sizes[0])
        w = int(sizes[1])
        h = int(sizes[2])
        sorted_numbers = sorted([l,w,h])
        smallest_two = sorted_numbers[:2]
        int1 = smallest_two[0]
        int2 = smallest_two[1]
        wrappingPaperSize += int1+int1+int2+int2
        wrappingPaperSize += l*w*h
    return(wrappingPaperSize)
    
print(assignemt2())