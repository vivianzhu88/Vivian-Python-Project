import random   # import the random library
heads = 0    # initialze variable called "heads"
for x in range (1,1000000):  # Set up a counter 1 to million
    y = random.randint(0,1)  # Generate random number
    if (y == 0):  # Zero corresponds to "heads"
        heads = heads + 1 # increment heads count by 1
print ("We got heads", heads, "times")   # print the total number of heads
