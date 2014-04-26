# Enter your code here. Read input from STDIN. Print output to STDOUT
#v  = input()
#m  = input()
#ar = [int(i) for i in raw_input().strip().split()]


def returnAr(l):
    ar = []
    for i in range(l):
        ar.append(i)
    return ar


def BinarySearch(ar, num):
    arL = len(ar)
    st = 0
    mid = (arL-st)/2
    i = 0
    
    while (arL-st) > 0:
        if ar[mid] > num:
            arL = mid
        elif ar[mid] < num:
            st = mid
        else:
            print mid
            return
        mid = (arL+st)/2
    
    print arL    

v = 333
ar = returnAr(999)    
            
BinarySearch(ar, v)