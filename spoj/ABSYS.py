def convertString(st):
	st = st.split('+')
	num1 = st[0].strip()
	st = st[1].split('=')
	num2 = st[0].strip()
	num3 = st[1].strip()

	if 'machula' in num1:
		num1 = (int(num3) - int(num2))
	elif 'machula' in  num2:
		num2 = (int(num3) - int(num1))
	else:
		num3 = (int(num1) + int(num2))

	print num1, '+', num2, '=', num3

t = input()
while t > 0:
	bl = raw_input()
	convertString(raw_input())
	t -= 1