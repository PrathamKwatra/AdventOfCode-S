FILE = "data_day_6_v2"
NEW_LINE = '\n'
EMPTYSTR = ''
newDict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

with open(FILE, "r") as fp:
    data = fp.readline()
    newList = []
    newString = EMPTYSTR
    while data:
        newString += data 
        data = fp.readline()
        if data == NEW_LINE or data==EMPTYSTR:
            newList.append(newString)
            newString = EMPTYSTR
 
for i in newList[:4]:
    pass
# STRINGS -> 
