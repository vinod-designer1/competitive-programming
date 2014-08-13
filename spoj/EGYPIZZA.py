import math
def minPiz(ar):
	noQ = 0
	noH = 0
	noTF = 0
	tP = 0
	for i in ar:
		if  i == '3/4':
			noTF += 1
		elif  i == '1/4':
			noQ += 1
		else:
			noH += 1
	tP = noTF
	noQ -= noTF
	if noH%2 == 0:
		num = noH/2
		tP += num
	else:
		num = noH/2
		tP += num + 1
		if noQ > 0:
			noQ -= 2

	if noQ > 0:
		tP += math.ceil(noQ/(4.0))
	return int(tP+1)

t = input()

if t == 0:
	print 1
else:
	ar = []
	while t > 0:
		bg = raw_input()
		el = raw_input()
		ar.append(el)
		t -= 1

	print minPiz(ar)
