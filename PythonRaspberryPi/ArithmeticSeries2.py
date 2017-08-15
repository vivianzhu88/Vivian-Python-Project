start = int(input("Enter the first term: "))
stop = int(input("Enter the last term: "))
increment = int(input("Enter the increment: "))
numterms = (stop-start)/increment +1

def sum (a,b,c):
    '''The function takes the first term, last term, and increment and finds
    the sum of arithmetic series'''
    q = (c*(a+b))/2
    return (q)

x = sum(start,stop,numterms)
print ("The sum of the series is:", x)
