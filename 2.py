s = 109
v = int(input('введи значение скорости: '))
t = int(input('введи значение времени: '))
s1 = v*t
if s1 <= s:
	print (s1)
else:
	while s1 > s:
		s1 -= s
	print(s1)	

		
