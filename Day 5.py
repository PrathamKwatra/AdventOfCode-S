FILE = "data_day_5"
NEWLINE = '\n'
EMPTYSTRING = ''
SEAT_ROW = list(range(128))
SEAT_COLUMN = list(range(8))
FRONT = 'F'
BACK = 'B'
LEFT = 'L'
RIGHT = 'R'

def seat_id(row, column):
   # print((row*8) + column)
    return (row*8) + column
def seat_row(string, SEAT_ROW):
    first_char = string[0] if string != '' else ''
    n = len(SEAT_ROW)//2
    if first_char == EMPTYSTRING:
       # print(SEAT_ROW)
        return SEAT_ROW[0]
    elif first_char == FRONT: 
       # print(SEAT_ROW)
        return seat_row(string[1:], SEAT_ROW[:n])
    elif first_char == BACK:
        #print(SEAT_ROW)
        return seat_row(string[1:], SEAT_ROW[n:])
def seat_col(string, SEAT_COLUMN):
    first_char = string[0] if string != '' else ''
    n = len(SEAT_COLUMN)//2
    if first_char == EMPTYSTRING:
       # print(SEAT_COLUMN)
        return SEAT_COLUMN[0]
    elif first_char ==  LEFT:
       # print(SEAT_COLUMN)
        return seat_col(string[1:], SEAT_COLUMN[:n])
    elif first_char == RIGHT:
        #print(SEAT_COLUMN)
        return seat_col(string[1:], SEAT_COLUMN[n:])

with open(FILE, "r") as fp:
    data = fp.readline()
    newString = EMPTYSTRING
    while data:
        newString += data 
        data = fp.readline()

newList = newString.split()
maxID = 0
iDList = []
for i in newList:
    row = seat_row(i[:7], SEAT_ROW)
    #print(i[:7], i[7:])
    col = seat_col(i[7:], SEAT_COLUMN)
    iD = seat_id(row, col)
##    if iD > maxID:
##        maxID = iD
##print(maxID)
    iDList.append(iD)
##print(iDList)


idSet = set(range(80,927))
print(idSet.difference(set(iDList)))
