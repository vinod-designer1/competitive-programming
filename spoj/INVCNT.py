cnt = 0
#need to implement in c
def mergeSort(ar, st, end):
	global cnt
	mid = (end + st) / 2
	if end-st > 0:
		l = mergeSort(ar, st, mid)
		r = mergeSort(ar, mid+1, end)

		a = []

		i = 0
		j = 0

		while i < (mid-st+1) and j < (end-mid):
			if r[j] >= l[i] :
				a.append(l[i])
				i += 1
			else:
				cnt += 1 * (mid-st+1-i)
				a.append(r[j])
				j += 1

		if i == (mid-st+1):
			while j < (end-mid):
				a.append(r[j])
				j += 1
		else:
			while i < (mid-st+1):
				a.append(l[i])
				i += 1

		return a
	else:
		return [ar[mid]]

t = input()
while t > 0:
	bg = raw_input()
	n = input()
	ar = []
	i = 0
	while i < n:
		ar.append(input())
		i += 1
	cnt = 0
	mergeSort(ar, 0, n-1)
	print cnt

	t -= 1