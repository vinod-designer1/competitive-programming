#https://www.hackerrank.com/challenges/triangle-numbers

#t = input()
#t = 10

def printTriangleTree(h):
	s = []
	ch = 0
	while h != 0:
		if (2*ch + 1) == 1:
			s.append(1)
		else:
			k = []
			i = -1
			lens = 2*(ch-1)+1
			while i < (2*ch):
				m = 0
				l = 0
				r = 0
				if 0 <= i < (lens) :
					m = s[i]

				if 0 <= (i+1) < (lens):
					r = s[i+1]

				if 0 <= (i-1) < (lens):
					l = s[i-1]

				k.append(m + l + r)
				
				i += 1
			s = k[:]

		end = ''

		for i in s:
			end += str(i)+ ' '

		print '  '*(h-1) + end
		ch += 1
		h -= 1


t = input()

while t > 0:
	n = input()
	
	if n%2 == 0:
		n = n/2
		if n%2 == 0:
			print 3
		else:
			print 4
	else:
		print 2
	t -= 1