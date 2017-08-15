debug = True
#If debug is true, then all of the functions would print out "evaluating function..." and print the result in the end
#If debug is false, then all of the functions wouldn't print out anything and just print the result
def function1(a,b):
    global debug
    if debug:
        print ("evaluating function1- Addition")
    return a+b

def function2(a,b):
    global debug
    if debug:
        print ("evaluating function2- Multiplication")
    return a*b

def function3(a,b):
    global debug
    if debug:
        print ("evaluating function3- Finding Remainder")
    return a%b

x = function1(4,5)
y = function2(4,5)
z = function3(5,4)

print(x,y,z)
