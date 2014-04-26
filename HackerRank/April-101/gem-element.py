char = [0]*26

gems = input()

i = gems
while i > 0:
	gem = raw_input()
	for cr in gem:
		el = ord(cr) - 97
		if char[el] == 0:
			char[el] = [0]*gems
		char[el][i-1] += 1
	i -= 1
cnt = 0
for el in char:
	gem = True
	if el != 0:
		for i in el:
			if i == 0:
				gem = False
				break
		if gem:
			cnt += 1
print cnt




