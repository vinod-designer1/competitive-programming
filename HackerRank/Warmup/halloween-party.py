#https://www.hackerrank.com/challenges/halloween-party
def max_choco_pieces(k):
	if k < 2:
		return 0
	mid = k/2
	rem = k - mid
	return mid * rem

t = input()

while t > 0:
	print max_choco_pieces(input())
	t -= 1