numlist = [1, 3, 4, 5, 9, 2]

for x in range (0,len(numlist)):
    for y in range (len(numlist)-1):
        if numlist[y]>numlist[y+1]:
            numlist[y],numlist[y+1] = numlist[y + 1],numlist[y]
print(numlist)


