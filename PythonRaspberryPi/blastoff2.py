import time

number = int (input ("Enter a number to count down from ")) #asks the user for a number to count down from

x=0
while (number > x): #while loop
    print (number - x) #countdown
    time.sleep(1) #1 second delay
    x = x+1
print ("Blast off!")
