n = 8#input()
st = '.LLLLL..'#raw_input()
s = -1
t = -1
l,r = st.rfind('L')+1, st.find('R')+1
if r > 0:
	print r, r + st.count('R')
else:
	print l, l - st.count('L')