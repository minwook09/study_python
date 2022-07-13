f = open('data.csv', 'w')
f.write('kim, lee, park')
f.write('\nkim, lee, park')
f.close()


list1 = ['samsung', 'kakao', 'naver', 'sinpong']

fin = open('fin.txt', 'w')
a=0
for i in list1:
    if a==0:
        fin.write(i)
        a=a+1
    else:
        fin.write('\n'+ i)
fin.close()


gogo = open ('gogo.txt', 'w')
count = 2
for i in range(0,8):
    for e in range(1,10):
        gogo.write (str(e * count) + '\n')
    count = count + 1


    