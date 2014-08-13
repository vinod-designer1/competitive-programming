def noApples(total, more):
	x = (total - more)/2
	print (x+more)
	print x

t = 10
while t > 0:
	noApples(input(), input())
	t -= 1