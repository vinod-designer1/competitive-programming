n = input()
if n < 3 :
	print n
else:	
	if n%2 == 1 :
		s =  n*(n-1)*(n-2)
	else:
		if n%3:
			s = n*(n-1)*(n-3)
		else:
			s = (n-1)*(n-2)*(n-3)
	print s