money = int (input ('What is the starting amount? ')) #starting amount
interest = float (input ('What is the interest rate? ')) #interest rate of 10%
years = int (input ('How many years do you want to invest for? ')) #number of years compounded
year = 1
total = money

f = open ("int.txt", "w")
while year <= years:
    total = total + (total*interest) # value each year
    f.write ('%2d %0.2f\n' % (year,total))
    year = year + 1
f.close()
