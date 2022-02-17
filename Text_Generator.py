import datetime

fh = open('Data.txt', 'w')
fh.write('Name: Jay Andrey Amulong \nAddress: Tokyo, Japan \nNumber: 09212121212')

Date = datetime.date.today()
Time = datetime.datetime.now()

print(Date)
print(Time)

fh.close()