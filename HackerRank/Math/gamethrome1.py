#https://www.hackerrank.com/challenges/game-of-thrones

chra = [0]*26

stng = raw_input()

for i in stng:
	chra[ord(i) - 97] += 1

odd = 0

for i in chra:
	if i%2 !=0:
		odd += 1

if odd > 1:
	print 'NO'
else:
	print 'YES'