eng2sp = dict ()
print(eng2sp) #prints out empty dictionary

eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}

eng2sp['two'] #commands for two and prints 'dos'
print(eng2sp)

eng2sp ['four'] = 'quatro'
print(eng2sp)

eng2sp ['one'] = 'un' #replaces 'one':'uno'
print(eng2sp)

del eng2sp ['one']
print(eng2sp)

eng2sp.clear()
print(eng2sp)

#in SHELL
#'two' in eng2sp (SHELL will print out 'True')
#'dos' in eng2sp (SHELL will print out 'False' because dictionary does not support search by values)

vals = eng2sp.values() #Then dictionary will support values
