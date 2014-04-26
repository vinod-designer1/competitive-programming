#https://www.hackerrank.com/challenges/chocolate-feast
def no_choc(n, c, m):
	nc = n/c
	wr = nc
	while wr/m > 0:
		nc += (wr/m)
		wr = (wr/m) + (wr%m)
	return nc

t = input()

while t > 0:
	ncm = [int(i) for i in raw_input().strip().split(' ')]
	print no_choc(ncm[0], ncm[1], ncm[2])
	t -= 1