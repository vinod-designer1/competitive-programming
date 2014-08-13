st = raw_input()
y = False
for i in st:
	if  i == 'H' or i == 'Q' or i == '9':
		y = True
		break
if y:
	print 'YES'
else:
	print 'NO'