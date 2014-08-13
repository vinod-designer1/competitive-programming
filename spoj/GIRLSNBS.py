## diving big number by small number to equal parts
import math
def minGenReg(b, g):
	if b==0 or g == 0:
		return (b+g)

	if b == g:
		return 1

	if b > g:
		b /= ((g+1) * 1.0)
		b = math.ceil(b)
		return int(b)

	if g > b:
		g /= ((b+1) * 1.0)
		g = math.ceil(g)
		return int(g)

bg = map(int, raw_input().split())

while bg[0] != -1:
	print minGenReg(bg[0], bg[1])

	bg = map(int, raw_input().split())



