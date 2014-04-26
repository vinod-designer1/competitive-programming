#http://math.stackexchange.com/questions/192177/how-many-times-to-roll-a-die-before-getting-two-consecutive-sixes

prb_l = [3]

avg_rolls = 2

j = 3

while j < 1001:
	prb_l.append((prb_l[j-3]*avg_rolls+1))
	j += 1

print prb_l

