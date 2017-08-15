import random

names = 'Aaron Bob Chris Daniel Ethan Fred Gargamel'
nameslist = names.split(' ') #Split string into a list

random.shuffle(nameslist) #Shuffle a list
print (nameslist) 

nameslist.append('Ivan') #Add to the end of list
print (nameslist)

nameslist.insert (2, 'Jack') #Add to a certain part of a list
print (nameslist)

print (min(nameslist)) #Min of a list
print (max(nameslist)) #Max of a list

nameslist.sort() #Sort a list
print (nameslist)
