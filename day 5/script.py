
def assignemt1():
    file = open('day 5/file.txt', 'r')
    lines = [line.strip() for line in file]
    pages,rules = getLists(lines)
    result = 0
    for rule in rules:
        valid = True
        for page in pages:
            if not checkRuleForPage(page,rule):
                valid = False
                break
        if valid:
            result += findMiddlePageNumber(rule)
    return result

def findMiddlePageNumber(rule):
    ruleArr = rule.split(',')
    mid = len(ruleArr) // 2  
    return int(ruleArr[mid])

def checkRuleForPage(page,rule):
    pageArr = page.split('|')
    ruleArr = rule.split(',')
    if pageArr[0] in ruleArr and pageArr[1] in ruleArr:
        index1 = ruleArr.index(pageArr[0])
        index2 = ruleArr.index(pageArr[1])
        if index1 > index2:
            return False
    return True

def getLists(lines):
    rules = []
    pages = []
    for line in lines:
        if '|' in line:
            pages.append(line)
        elif len(line) > 0:
            rules.append(line)
    return (pages,rules)

print(f'assignemt 1: {assignemt1()}')
