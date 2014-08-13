def revPolishNot(exp):
	varStack = []
	tempStack = []
	for i in exp:
		aciI = ord(i)
		if 97 <= aciI and aciI <= 122 :
			varStack.append(i)
		elif i != '(' and i != ')' :
			tempStack.append(i)
		elif i == ')':
			varStack.append(tempStack.pop())
	while tempStack:
		varStack.append(tempStack.pop())
	s = ''
	for i in varStack:
		s += i
	return s

t = input()
while t > 0:
	print revPolishNot(raw_input())
	t -= 1
