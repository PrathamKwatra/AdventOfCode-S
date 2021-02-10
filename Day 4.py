import re
#Passport Checker
FILE = "data_day_4"
NEWLINE = '\n'
EMPTYSTRING = ''

with open(FILE, "r") as fp:
    data = fp.readline()
    newString = EMPTYSTRING
    newList = []
    while data:
        if data == NEWLINE:
            newList.append(newString)
            newString =EMPTYSTRING
        else:
            newString += data 
        data = fp.readline()
    newList.append(newString)

def dataValidity(string):
    toCheck = string.split()
    checkPass = 0
    for i in toCheck:
        node = i[:3]
        data = i[4:]
        
        if node != "cid":
            if node == 'byr':
                toMatch = re.compile('(\d+)')
                if toMatch.match(data) and len(data) == 4:
                    if int(data) in range(1920, 2003):
                        checkPass += 1
                    else:
                        print('FAULT IN BYR')
            if node == 'iyr':
                toMatch = re.compile('(\d+)')
                if toMatch.match(data) and len(data) == 4:
                    if int(data) in range(2010, 2021):
                        checkPass += 1
                    else:
                        print('FAULT IN IYR')

            if node == 'eyr':
                toMatch = re.compile('(\d+)')
                if toMatch.match(data) and len(data) == 4:
                    if int(data) in range(2020, 2031):
                        checkPass += 1
                    else:
                        print('FAULT IN EYR')

            if node == 'hgt':
                unit = data[-2:]
                hgt = data[:-2]
                if unit == 'cm':
                    if int(hgt) in range(150, 194):
                        checkPass += 1
                elif unit == 'in':
                    if int(hgt) in range(59, 77):
                        checkPass += 1
                else:
                    print('FAULT IN HGT')
            if node == 'hcl':
                toMatch = re.compile('^#[0-9a-f]{6}')
                isMatch = toMatch.match(data)
                if toMatch and len(data) == 7:
                    checkPass += 1
                else:
                    print('FAULT IN HCL')
            if node == 'ecl':
                if data in "amb blu brn gry grn hzl oth".split():
                    checkPass += 1
                else:
                    print('FAULT IN ECL')
            if node == 'pid':
                toMatch = re.compile('(\d+)')
                if toMatch.match(data) and len(data) == 9:
                    checkPass += 1
                else:
                    print('FAULT IN PID')

    if checkPass == 7:
        print('\n ^ TRUE\n')
        return True
    else:
        print('\n ^ FALSE\n')
    return False

def passportValid(string):
    conditionCheck = [string.count("byr"),
                      string.count("iyr"),
                      string.count("eyr"),
                      string.count("hgt"),
                      string.count("hcl"),
                      string.count("ecl"),
                      string.count("pid"),
                      string.count("cid")]
    firstCondition = False
    if min(conditionCheck[:-1]) != 0:
        firstCondition = True
    if firstCondition:
        return dataValidity(string)
    print('\n ^ False\n')
    return False

ValidPassCnt = 0
for i in newList:
    print(i)
    if passportValid(i):
        ValidPassCnt += 1

print(ValidPassCnt)
