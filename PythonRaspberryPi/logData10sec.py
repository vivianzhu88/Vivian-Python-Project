from random import randint
import time
import datetime

f = open ('numbers1.txt','a')

for i in range (1,6):
    time.sleep(1)
    f.write (str(randint(1,10)) +"\n")
    
print ("I am done!")
f.close()


#while True:
#    x = (random.randint(0,26))   # Generate a random number
#    print (x)   # Printing to cross check the File created
#    y = str(x)  # Converting the number to a string 
#    time.sleep(5)  # Waiting for 5 seconds before the next run
#    with open('randint.txt','a') as myfile:  # Opened an Appendable file
#        myfile.write(y)             # Write to the file
    
