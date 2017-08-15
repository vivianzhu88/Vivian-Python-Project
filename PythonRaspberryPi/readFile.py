filename = open ('random.txt', 'w') #'w' = writable file
filename.write ('Hi, my name is Vivian') #writes into a file
filename.close() #closes file after use

f2 = open ("readme.txt", "r") #'r' = readable file
line = f2.readline() #saves read line into variable
print(line) #prints out saved line
f2.close()

f = open ("readme.txt", "r")
print (f.read(5)) #prints out 5 characters
f.close()

#When you close file, you remove the bookmark from the file
