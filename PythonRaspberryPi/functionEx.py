count = 0

def count1():
    global count #it is a global variable and refers to count = 0
    count = count + 1
    count = count + 1
    return count

def count2():
    global count #it is a global variable and refers to count = 2 because it is after count1 and the result of count1 is 2 
    count = count * 4
    return count

def count3():
    count = 1 #since it is a local variable, the function ignores value of count and you have to define it
    count = count + 2
    return count #you can return a variable

x = count1()
y = count2()
z = count3()

print (x,y,z)

def hi (a,b):
    return a+b #you can return a product of the program

print(hi(5,6))
