def histogram(s):
    d = dict () #Define Dictionary 'd'
    for i in s:
        if i not in d: #We have not come across this character earlier
            d[i] = 1
        else:
            d[i] = d[i] + 1
    return (d)

def search_hist(a,b):
    if a in b:
        print ('Character:', a)
        print ('Count:', b[a])
    else:
        b = 0
        print ('Character:', a)
        print ('Count:', b)

x = input ('Enter a string: ')
hist = histogram (x)
y = input ('Choose a character: ')
search_hist (y, hist)




#def print_hist(h): #Prints in a vertical list
#    for i in h:
#        print (i, h[i])


#print_hist (histogram ('tyrannosaurus rex'))

#eng2sp = {'one':'uno', 'two':'dos', 'three':'tres', 'four':'cuatro'}
#print hist (eng2sp)
