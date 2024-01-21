from datetime import datetime

a = '2024-01-20 23:02:38'
b = datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
c = datetime.strptime(a, '%Y.%m.%d %H:%M:%S')
print(b)


#
# if datetime.datetime.strptime(date, "%d.%m.%Y):
#    print "it's a date"
# else:
#    print date