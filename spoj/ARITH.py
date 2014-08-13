def reduceZero(res):
	lenR = len(res)
	i = 0
	while i < lenR and res[i] == '0':
		i += 1
	if i == lenR:
		return ' ' * (i-1) + '0' 
	return ' ' * i + res[i:]

def add(a,  b):
	c = 0
	b = '+' + b
	aLen = len(a)
	bLen = len(b)
	maxLen = bLen
	if aLen > bLen:
		maxLen = aLen
		b = (' ') * (maxLen - bLen) + b
	else:
		a = (' ') * (maxLen - aLen) + a

	dash = '-' * (maxLen)
	addR = ''

	i = maxLen - 1
	while i >= 0:
		x = a[i]
		if x == ' ':
			x = 0
		y = b[i]
		if y == ' ' or y == '+':
			y = 0
		psum = c + int(x) + int(y)
		c = psum/10
		psum = psum%10
		addR = str(psum) + addR
		i -= 1

	if addR[0] == '0':
		addR = addR[1:]
	if c != 0:
		addR = str(c) + addR
	else:
		addR = ' ' + addR

	return (addR, a, b, dash)

def subtract(a, b):
	c = 0
	b = '-' + b
	aLen = len(a)
	bLen = len(b)
	maxLen = aLen
	if bLen > maxLen:
		maxLen = bLen
	b = (' ') * (maxLen - bLen) + b
	a = ' ' * (maxLen - aLen) + a
	dash = '-' * (maxLen)
	subR = ''

	i = maxLen - 1
	while i >= 0:
		x = a[i]
		if x == ' ':
			x = 0
			break

		y = b[i]
		if y == ' ' or y == '-':
			y = 0

		x = c+int(x)
		y = int(y)
		if x < y:
			x = 10 + x		
			c = -1
		else:
			c = 0

		r = x-y
		subR = str(r) + subR
		i -= 1

	subR = reduceZero(subR)

	print a
	print b
	print dash

	print ' ' * (maxLen - aLen) + subR


def multiply(a, b):
	c = 0
	b = '*' + b
	aLen = len(a)
	bLen = len(b)
	multiR = ''
	res = ['']*(bLen-1)

	i = bLen - 1
	j = 0

	while i > 0:
		k = aLen - 1
		c = 0
		while k >= 0:
			p = int(b[i]) * int(a[k])
			p += c
			c = p / 10
			res[j] = str(p%10) + res[j]
			k -= 1

		if c != 0:
			res[j] = str(c) + res[j]

		j += 1
		i -= 1

	i = 0
	addR = ''

	while i < bLen-1:
		res[i] = str(int(res[i]))
		res[i] = res[i] + ' ' * i
		addR = add(addR, res[i])[0]
		i += 1

	addR = addR.strip()
	addR = reduceZero(addR)

	lenR = len(addR)
	maxL = aLen
	minL = bLen-1
	maxA = lenR

	if bLen > aLen:
		maxL = bLen
		minL = aLen

	if maxA < maxL:
		maxA = maxL


	a = ' ' * (maxA - aLen) + a
	b = ' ' * (maxA - bLen) + b
	dash = ' ' * (maxA - maxL) + '-' * (maxL)
	print a
	print b

	if minL > 1:
		print dash

		i = 0
		while i < bLen-1:
			res[i] =  ' ' * (maxA - len(res[i])) + res[i]
			print res[i]
			i += 1
	print '-' *  (maxA)
	print  ' ' * (maxA - lenR) + addR

def simpleAirthmatics(st):
	ab = ['', '']
	op = ''
	i = 0
	for s in st:
		if s != '+' and s != '-' and s != '*':
			ab[i] += s
		else:
			op = s
			i += 1
	if op == '+':
		result = add(ab[0], ab[1])
		print result[1]
		print result[2]
		print result[3]
		print result[0]
	elif op == '-':
		subtract(ab[0], ab[1])
	else:
		multiply(ab[0], ab[1])

t = input()
while t > 0:
	simpleAirthmatics(raw_input())