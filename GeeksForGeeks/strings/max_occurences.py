def max_char_occurences(s):
	ar = [0]*26
	for c in s:
		if c != ' ':
			ar[ord(c)-97] += 1
	maxv = 0
	maxc = 0
	i = 0
	while i < 26:
		if maxv < ar[i]:
			maxv = ar[i]
			maxc = i
	return str(unichr(maxc+97))