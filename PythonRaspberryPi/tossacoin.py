import random # import the random library
print (random.randint (1,6))

heads = 0 # initialize variable called "heads"

for x in range (1,1000000): # set up a counter 1 to million
    y = random.randint(0,1) # generate a random number
    if y == 0: # zero corresponds to "heads"
        heads = heads + 1
print (heads)
