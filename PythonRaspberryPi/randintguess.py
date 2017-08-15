import random
count = 0;

for x in range (1,11): #run for 10 times
    y = random.randint (1,3) #guess a number 1,2,3
    z = int (input("Enter a number from 1 to 3: "))
    if (y == z): #computer's number and your number
        print ("Correct!")
        count += 1
    else:
        print ("Incorrect!")
print ()
print ("You scored", count, "out of 10")
if count >= 3:
    print ("You win!")
else:
    print ("The computer wins!")

    
