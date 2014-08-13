from Queue import *

def contSeq(mT, ht, bdt):
	i = 0
	j = 0
	maxL = 0
	while i < ht:
		j = 0
		while j < bdt:
			if mT[i][j] == 'A':
				q = Queue()
				q.put([i, j, 1])
				if maxL < 1:
					maxL = 1
				while not q.empty():
					crd = q.get()
					crtL = crd[2]

					right = [crd[0], crd[1]+1] if crd[1]+1 < bdt else []
					left = [crd[0], crd[1]-1] if crd[1] > 0 else []
					top = [crd[0]-1, crd[1]] if crd[0] > 0 else []
					bottom = [crd[0]+1, crd[1]] if crd[0]+1 < ht else []

					topRight = [crd[0]-1, crd[1]+1] if crd[0] > 0 and crd[1]+1 < bdt else []
					topLeft = [crd[0]-1, crd[1]-1] if crd[1] > 0 and crd[1] > 0 else []
					bottomRight = [crd[0]+1, crd[1]+1] if crd[0]+1 < ht and crd[1]+1 < bdt else []
					bottomLeft = [crd[0]+1, crd[1]-1] if crd[0]+1 < ht and crd[1] > 0 else []

					if right:
						prs = right
						r = mT[prs[0]][prs[1]]
						if (ord(r) - ord('A')) == crtL:
							q.put([prs[0], prs[1], crtL+1])

							if maxL < crtL+1:
								maxL = crtL+1

					if left:
						prs = left
						r = mT[prs[0]][prs[1]]
						if (ord(r) - ord('A')) == crtL:
							q.put([prs[0], prs[1], crtL+1])

							if maxL < crtL+1:
								maxL = crtL+1

					if top:
						prs = top
						r = mT[prs[0]][prs[1]]
						if (ord(r) - ord('A')) == crtL:
							q.put([prs[0], prs[1], crtL+1])

							if maxL < crtL+1:
								maxL = crtL+1

					if bottom:
						prs = bottom
						r = mT[prs[0]][prs[1]]
						if (ord(r) - ord('A')) == crtL:
							q.put([prs[0], prs[1], crtL+1])

							if maxL < crtL+1:
								maxL = crtL+1

					if topLeft:
						prs = topLeft
						r = mT[prs[0]][prs[1]]
						if (ord(r) - ord('A')) == crtL:
							q.put([prs[0], prs[1], crtL+1])

							if maxL < crtL+1:
								maxL = crtL+1

					if topRight:
						prs = topRight
						r = mT[prs[0]][prs[1]]
						if (ord(r) - ord('A')) == crtL:
							q.put([prs[0], prs[1], crtL+1])

							if maxL < crtL+1:
								maxL = crtL+1

					if bottomLeft:
						prs = bottomLeft
						r = mT[prs[0]][prs[1]]
						if (ord(r) - ord('A')) == crtL:
							q.put([prs[0], prs[1], crtL+1])

							if maxL < crtL+1:
								maxL = crtL+1

					if bottomRight:
						prs = bottomRight
						r = mT[prs[0]][prs[1]]
						if (ord(r) - ord('A')) == crtL:
							q.put([prs[0], prs[1], crtL+1])

							if maxL < crtL+1:
								maxL = crtL+1
			j +=1
		i += 1
	return maxL

hb = map(int, raw_input().strip().split(' '))
j = 1
while hb[0] > 0 and hb[1] > 0:
	h = hb[0]
	b = hb[1]
	i = 0
	mT = []
	while i < h:
		mT.append(list(raw_input().strip()))
		i += 1
	print 'Case', str(j)+':', contSeq(mT, h, b)
	
	hb = map(int, raw_input().strip().split(' '))
	j += 1