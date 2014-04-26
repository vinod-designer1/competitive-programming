
import random


#k = input()

#ar = [int(i) for i in raw_input().strip().split(' ')]


for i in range(3,4):
	#ar = random.sample(xrange(100), i)
	ar  = [95, 94, 90]
	ar.sort(reverse=True)

	print ar

	days = 0
	daysLeft = 0

	for d in ar:
		need = d+1
		if daysLeft < need:
			daysLeft = d - daysLeft
			days += daysLeft + 1
		else:
			daysLeft = daysLeft - need

	print days + 1