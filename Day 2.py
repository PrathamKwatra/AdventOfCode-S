#Password Checker
#conditions - if given string is "14-22 g: lglllgllglglgg", then the password is valid if g is present on 13 XOR g is present on 21.
FILE = "data_day_2"

def formatted(string):
    temp = string.split()
    temp[0] = temp[0].split("-")
    temp[0][0] = int(temp[0][0]) - 1 
    temp[0][1] = int(temp[0][1]) - 1 
    temp[1] = temp[1][:-1]
    return temp
    
with open(FILE, "r") as fp:
    data = fp.readline()
    newList = []
    while data:
        newList.append(formatted(data))
        data = fp.readline()

cnt = 0
for i in newList:
    if (i[2][i[0][0]] == i[1] or i[2][i[0][1]] == i[1]) and (not ( i[2][i[0][0]] == i[1] and i[2][i[0][1]] == i[1])):
        print("V", end='\n')
        cnt += 1
    else:
        print("F")

print (cnt)
