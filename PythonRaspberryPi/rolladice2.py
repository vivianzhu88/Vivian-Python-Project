import random   # import the random library
num = 0    # initialze variable called "num"
for x in range (1,1000000):  # Set up a counter 1 to million
    y = random.randint(1,6)  # Generate random number
    if (y == 2) or (y == 3):  # num corresponds with two and three
        num = num + 1 # increment number count by 1
print ("We got 2 and 3", num, "times")   # print the total number of twos

