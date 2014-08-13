def countSort(ar):
	p = [0] * 11

	for i in ar:
		p[i] += 1

	i = 0
	sar = []
	while i < 11:
		sar += [i] * p[i]
		i += 1
	return sar

def fashinoRateSum(m, w, p):
	m = countSort(m)
	w = countSort(w)

	i = 0
	sumF = 0

	while i < p:
		sumF += (m[i] * w[i])
		i += 1

	return sumF

t = input()

while t > 0:
	p = input()
	m = [int(i) for i in raw_input().strip().split(' ')]
	w = [int(i) for i in raw_input().strip().split(' ')]

	print fashinoRateSum(m, w, p)

	t -= 1