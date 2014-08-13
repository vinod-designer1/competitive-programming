def passwordStrength(passw):
	le = len(passw)
	isS = False
	isL = False
	isN = False
	if le < 5:
		return 'Too weak'
	else:
		for i in passw:
			if  i <= 'z' and i >= 'a':
				isS = True
			elif i <= 'Z' and i >= 'A':
				isL = True
			elif i <= '9' and i >= '0' :
				isN = True

			if isS and isL and isN:
				return 'Correct'
		return 'Too weak'

print passwordStrength(raw_input())