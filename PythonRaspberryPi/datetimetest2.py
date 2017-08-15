import time
import datetime
from random import randint


f = open ('numbers2.txt','a')
time2 = datetime.datetime.now().strftime("%y - %m - %d -%H - %M")
for i in range (1,6):
    time.sleep(10)
    
    x = str(randint(1,10))
    
    print(x)    
    print(time2)
    f.write (x + "\t")
    f.write (time2 +"\n")
    
print ("I am done!")
f.close()