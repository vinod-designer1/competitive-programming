
def anagrams(s1, s2, st, end):
	c1 = [0] * 26
	c2 = [0] * 26

	nlen = end - st

	cnt = 0

	for c in s1:
		c1[ord(c) - 97] += 1
		
	i = st
	while i < end:
		c = s2[i]
		ind = ord(c) - 97
		if c1[ind] == 0:
			return False
		c2[ind] += 1
		i += 1
	
	i = 0
	while i < 26:
		if c1[i] == c2[i]:
			cnt += c1[i]
		i += 1
	if cnt == nlen:
		return True
	else:
		return False

def getUniqNum(s1, s1len):
	i = 0
	sum1 = 0
	while i < s1len:
		sum1 += (ord(s1[i]) - 97)
		i += 1

	return sum1


k = input()
#k = 3
#ar = [['hack', 'indiahacks'],['code','eddy'],['coder','iamredoc']]


for i in range(k):
	s1 = raw_input()
	s2 = raw_input()
	#s1 = ar[i][0]
	#s2 = ar[i][1]

	s1len = len(s1)
	s2len = len(s2)

	sums = getUniqNum(s1, s1len)

	ex = 0

	i = 0

	sumn = 0

	while i < (s2len-s1len+1):
		if i == 0:
			j = 0
			while j < s1len:
				sumn +=  (ord(s2[i+j]) - 97)
				j += 1
		else:
			sumn = sumn + (ord(s2[i+s1len-1])) - (ord(s2[i-1]))

		if sumn == sums:
			if anagrams(s1, s2, i, i+s1len):
				ex = 1
				break;

		i += 1

	if ex == 0:
		print 'NO'
	else:
		print 'YES'



