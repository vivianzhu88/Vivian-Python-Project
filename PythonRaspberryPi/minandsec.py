seconds = int (input ("How many seconds? ")) #asks the user for seconds to convert to hours, minutes, and seconds
print (seconds, "seconds =", seconds//3600, "hour(s),", ((seconds//60) - ((seconds//3600)*60)), "minute(s), and", seconds%60, "seconds") #uses mod & div to convert the seconds to hours, minutes, and seconds
