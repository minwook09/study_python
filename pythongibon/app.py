file = open('a.txt', 'w')
file.write('hellow')
file.close()

file = open ( 'a.txt', 'a' ) 
file.write('\nfuckyou')
file.close()

file = open('a.txt', 'r')
print( file.read() )
file.close()
