def remove_duplicates(s):
	ar = [0]*26
	for c in s:
		ar[ord(c)-97] += 1
	k = ''
	i = 0
	while i < 26:
		if ar[i] >= 1:
			k += str(unichr(i+97))
	return k

def return_all_duplicates(s):
	ar = [0]*26
	for c in s:
		ar[ord(c)-97] += 1
	k = []
	i = 0
	while i < 26:
		if ar[i] > 1:
			k.append(str(unichr(i+97)))
	return k
