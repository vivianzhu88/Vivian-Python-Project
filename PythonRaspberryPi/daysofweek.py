from time import sleep

days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'

days_list = days.split()

for days in days_list:
    print (days)
    if (days == 'Saturday' or days == 'Sunday'):
           print ("Hooray!")
    sleep(1)
