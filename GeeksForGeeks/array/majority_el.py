from random import randint
#Moores Voting Algorithm
def findCandidate(ar, n):
	maj_index = 0
	i = 1
	count = 1
	while i < n:
		if ar[maj_index] == ar[i]:
			count += 1
		else:
			count -= 1

		if count == 0:
			maj_index = i
			count = 1
		i += 1
	return ar[maj_index]

def isMajority(ar, n, el):
	count = 0
	for nu in ar:
		if nu == el:
			count += 1
	return count

def getMajority(ar, n):
	num = findCandidate(ar, n)

	print num

	count = isMajority(ar, n, num)

	if count >= n/2:
		return num
	else:
		return -1

def random_ary(sz):
	ar = []
	for i in range(sz):
		ar.append(randint(-1000, 1000))
	return ar

def test_Majority(n):
	i = 0
	while i < n:
		ar = random_ary(10)
		ar = [2,2,1,3,5,4,6,7,8,9]
		print ar
		print getMajority(ar, 10)
		i += 1
test_Majority(1)


