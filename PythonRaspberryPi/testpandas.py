import pandas as pd

df = pd.read_csv('iris.csv', header = 1, nrows = 151)
#Makes Row #n as header
print (df)

df = pd.read_csv('iris.csv', header = None, nrows = 150)
#Assigns column number as header for column
print (df)

df = pd.read_csv('iris.csv', header = 0, nrows = 150)
#Makes Row 0 as header // first line
print (df)

