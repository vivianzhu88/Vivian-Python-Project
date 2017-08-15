import random

colors = 'orange pink indigo green red yellow blue magenta cyan'
colorslist = colors.split() #Split a string into a list

random.shuffle(colorslist) #Shuffle a list
print ('The shuffled list:', colorslist)

print ('The minimum is:', min(colorslist)) #Minimum of list
print ('The maximum is:', max(colorslist)) #Maximum of list

colorslist.sort() #Sort list from min to max
print ('The sorted list:', colorslist)

colorslist.insert (5, 'violet') #Insert a string at a certain position in list
print ('Insert in list:',colorslist)

colorslist.append ('brown') #Add string to the end of list
print ('Appended list:',colorslist)

print ('Count of red:', colorslist.count('red')) #Count how many times 'red' appears in list

colorslist.pop (1) #Remove one string in a certain position of list
print ('Pop from list:', colorslist)

colorslist.remove ('green') #Remove certain string from list
print ('Remove from list:', colorslist)

colorslist.reverse() #Reverse the list
print ('Reverse the list:', colorslist)

list2 = ['A', 'B', [1, 2, 3], 'C']
print (list2[1])
print (list2[2][0])
