import time
import datetime

a= time.time()
a= time.ctime(a)

a = time.localtime()
p = time.strftime('%Y year %m month', a )
#print(p)

name = 'kim'
#print('안녕하세요 %s'%name)
#print(f'안녕하세요 {name}')

time1 = datetime.datetime(2022, 10 ,1 )
print(time1)