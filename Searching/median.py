#!/bin/python
def findIndex(s, item, slen):
	st = 0
	en = slen
	while (en - st) > 0 :
		#print 'end: ' + str(en) + ' ' + 'st: ' + str(st)

		mid  = (en+st)/2

		if s[mid] > item:
			en = mid - 1
		elif s[mid] < item:
			st = mid + 1
		else:
			return mid
	return en

def median(a,x):
	s = []
	c = 0
	wrong = False
	for i in range(len(a)):
		if a[i] == 'a':
			if c == 0:
				s.append(x[i])
			else:
				indx = findIndex(s, x[i], c-1)
				#print 'add: ' + str(indx)
				if indx == c-1:
					s = s[:]+[x[i]]
				elif indx == 0:
					s = [x[i]] + s[0:]
				else:
					s = s[:indx+1]+[x[i]]+s[indx+1:]
			c += 1
		elif a[i] == 'r':
			indx = findIndex(s, x[i], c-1)
			#print 'remove: ' + str(indx)

			if indx >=0 and indx < c:
				if s[indx] != x[i]:
					wrong = True
				else:
					if indx > 0:
						if indx == c-1:
							s = s[:indx]
						else:
							s = s[:indx]+s[indx+1:]
					else:
						s = s[1:]
					c -= 1
			else:
				wrong = True

		if wrong:
			print 'Wrong!'
			wrong = False
		else:
			if c > 0:
				if c%2 == 0:
					mid = (c-1)/2
					median = (s[mid]+s[mid+1])/2.0
				else:
					median = s[(c-1)/2]

				if median == int(median):
					median = int(median)
				print median
			else:
				print 'Wrong!'

		#print s




N = input()
s = []
x = []
for i in range(0, N):
   tmp = raw_input().strip().split(' ')
   a, b = [xx for xx in tmp]
   s.append(a)
   x.append(int(b))
median(s,x)