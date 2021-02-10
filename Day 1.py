newList = []
target = 0

for i in range(len(newList)): ##newList is sorted
	temp = [target - newList[i] for j in temp]
	temp = [temp[j] - newList[j] for j in range(1, len(temp))]
	set(temp).intersection(set(newList))

#hash the entire list
#two for loops
	
