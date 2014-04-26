#https://www.hackerrank.com/challenges/utopian-tree
def tree_height(n):
	s = 0
	h = 1
	while s < n:
		if s%2 == 0:
			h *= 2
		else:
			h += 1
		s += 1
	return h

t = input()

while t > 0:
	print tree_height(input())
	t -= 1