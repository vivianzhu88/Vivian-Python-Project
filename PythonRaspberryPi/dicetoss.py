import random   # import the random library
twos = 0    # initialze variable called "twos"
for x in range (1,1000000):  # Set up a counter 1 to million
    y = random.randint(1,6)  # Generate random number
    if (y == 2):  # Two corresponds with two"
        twos = twos + 1 # increment twos count by 1
print ("We got 2", twos, "times")   # print the total number of twos
