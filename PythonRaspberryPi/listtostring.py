days_week = 'Monday Tuesdy Wednesday Thursday Friday Saturday Sunday'
days_week_list = days_week.split()
print (days_week_list)
y = days_week_list.index('Friday')
print (y)
days_week_list[y] = 'Saturday'
print (days_week_list)
