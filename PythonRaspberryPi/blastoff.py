import time

count = int (input ("Enter a number to count down from ")) #asks the user for a number to count down from

for x in range (count,0,-1): #range
    print (x) #prints range from count to 0
    time.sleep(1) #wait for 1 second
print ("Blast off!")
