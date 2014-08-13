import math
def findVal(st):
	calc = st.split()
	
	val = int(calc[0])

	i = 1
	calL = len(calc)

	while i < calL:
		if calc[i] == '+':
			val += int(calc[i+1])
		elif calc[i] == '*':
			val *= int(calc[i+1])
		elif calc[i] == '-':
			val -= int(calc[i+1])
		elif calc[i] == '/':
			val /= int(calc[i+1])
		i += 2
	return val

t = input()
while t > 0:
	bl = raw_input()
	print findVal(raw_input())

	t -= 1