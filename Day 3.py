FILE = "data_day_3"
X = 1
Y = 1
CHAR = '#'

with open(FILE, "r") as fp:
    data = fp.readline()
    newString =''
    while data:
        newString += data 
        data = fp.readline()

newList = newString.split()

for i in range(len(newList)):
    newList[i] = newList[i]*6

maxX = len(newList[0])
maxY = len(newList)

tempX = 0
tempY = 0

trees = 0

while (tempY+Y) < maxY:
    tempX += X
    tempY += Y
    if tempX >= maxX:
        tempX = tempX - maxX
    string = newList[tempY]
    if string[tempX] == CHAR:
        trees += 1
print(trees)
