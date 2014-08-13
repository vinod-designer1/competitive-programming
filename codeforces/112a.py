st1 = raw_input().lower()
st2 = raw_input().lower()
stL = len(st1)
big = False
for i in range(0, stL):
	if st1[i] >  st2[i]:
		print 1
		big = True
		break
	elif st1[i] <  st2[i]:
		print -1
		big = True
		break

if not big:
	print 0