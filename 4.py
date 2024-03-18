a = int(input('введи 1 число: '))
b = int(input('введи 2 число: '))
c = int(input('введи 3 число: '))

if (a==b and b==c):
	print ('3')
elif (a==b or a==c):
	print ('2')
elif b==c:
	print('2')	
else:
	print ('0')
		
