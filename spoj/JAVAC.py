import sys

def convertJCOrCJ(st):
	stL = len(st)
	i = 0
	jf = False
	cf = False

	if st[stL-1] == '_':
		return 'Error!'

	if st[0] == '_':
		return 'Error!'

	if st[0] >= 'A' and st[0] <= 'Z':
		return 'Error!'

	while i < stL:
		if st[i] == '_' or (st[i] >= 'A' and st[i] <= 'Z'):
			if not jf and not cf:
				if st[i] == '_':
					jf = True
					if st[i+1] >= 'a' and st[i+1] <= 'z':
						jf = True
						st = st[:i] + st[i+1].upper() + st[i+2:]
						i += 1
						stL -= 1
					else:
						return 'Error!'
				else:
					cf = True
					st = st[:i] + '_' + st[i].lower() + st[i+1:]
					i += 2
					stL += 1
			elif jf:
				if st[i] == '_':
					if st[i+1] >= 'a' and st[i+1] <= 'z':
						jf = True
						st = st[:i] + st[i+1].upper() + st[i+2:]
						i += 1
						stL -= 1
					else:
						return 'Error!'
				else:
					return 'Error!'
			elif cf:
				if st[i] == '_':
					return 'Error!'
				else:
					st = st[:i] + '_' + st[i].lower() + st[i+1:]
					i += 2
					stL += 1


		elif not (st[i] >= 'a' and st[i] <= 'z'):
			return 'Error!'
		else:
			i += 1

	return st

while 1:
    next = sys.stdin.readline().strip()
    if not next:
    	break
    print convertJCOrCJ(next)