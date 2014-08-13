def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return mid
    return -1

def binary_search_approx(l, value):
    low = 0
    high = len(l)-1
    while low + 1 < high:
        mid = (low+high)//2
        if l[mid] > value:
            high = mid
        elif l[mid] < value:
            low = mid
        else:
            return mid
    return high if abs(l[high] - value) < abs(l[low] - value) else low

n = input()
ar=sorted([int(raw_input()) for i in range(n)])
mid = n//2 - 1
r = n - 1
s = 0
while mid >= 0:
	if ar[mid]*2 <= ar[r]:
		r -= 1
		s += 1
	mid -= 1
print n-s