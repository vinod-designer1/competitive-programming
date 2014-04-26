def solution(R, X, M):
    # write your code in Python 2.6
    max_bots = (M-2)/4
    max_distance = 0
    r_len = len(R)
    if r_len > max_bots:
        return -1
    k = 0
    for i in R:
        p = (i-2)/4
        if (i-2)%4 == 0:
            s = 0
        else:
            if i - (4*p+2) > 0:
                s = ((4*(p+1)+2) - i)
            else:
                s = ((4*(p)+2) - i)
                
        if s > max_distance:
            max_distance = s
            
        k += 1
    
    return max_distance

#([4, 7, 9, 11, 14, 21, 21, 22, 22, 23], 1, 37)
#with WRONG ANSWER [ got -1 expected 3 ] 