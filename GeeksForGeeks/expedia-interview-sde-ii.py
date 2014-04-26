def k_largest_matrix(arr, m, n, k):
	'''
		Given MxN matrix with sorted elements row wise and column wise, 
		find the Kth largest element
	'''
	mid = [m/2, n/2]
	pass

def find_matrix(arr, stm, stn, em, en, el):
	'''
		Given MxN matrix with sorted elements row wise and column wise, 
		find an element
	'''
	if stm-em == 0 or stn-en == 0:
		if arr[stm, en] == el:
			return (stm, en)
		else:
			return -1
	else:
		mid = [(stm+em)/2, (stn+en)/2]
		if arr[mid[0], mid[1]] > el:
			em = mid[0]
			en = mid[1]
		elif arr[mid[0], mid[1]] < el:
			stm = mid[0]
			stn = mid[1]
		else:
			return (mid[0], mid[1])
		return find_matrix(arr, stm, stn, em, en, el)

def find_max_1(arr, stm, stn, em, en):
	'''
		Given MxN matrix which contains 1s and 0s,
		find the largest sub matrix which contains most number of 1s. 
		condition is that each row in the sub matrix must contain at-least one 1
	'''
	if stm-em == 0 or stn-en == 0:
		if arr[stm, en] == 1:
			return (stm, en)
		elif arr[stm+1, en] == 1:
			return (stm+1, en)
		elif arr[stm+1, en+1] == 1:
			return (stm+1, en+1)
		elif arr[stm, en+1] == 1:
			return (stm, en+1)
		else:
			return -1
	else:
		mid = [(stm+em)/2, (stn+en)/2]
		if arr[mid[0], mid[1]] == 1:
			em = mid[0]
			en = mid[1]
		elif arr[mid[0], mid[1]] == 0:
			stm = mid[0]
			stn = mid[1]
		return find_max_1(arr, stm, stn, em, en)

def intersect_list(li1, li2):
	'''
		Given two Linked lists, find out whether they intersect or not
		and where do they intersect
	'''
	pass