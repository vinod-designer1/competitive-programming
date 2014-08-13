#sol 2040290
def noOfPos(ar, n):
    cnt = 1
    prev = -1
    tot = 0
    sort = [ar[0]]
    total = 0
    for i in ar:
        if prev != -1:
            if prev < i:
                cnt += 1
                sort.append(i)
            else:
                #print sort, cnt
                total += cnt
                sort = [i]
                tot += (cnt * (cnt+1))/2
                cnt = 1
        prev = i
    #print sort
    #total  += cnt
    tot += (cnt * (cnt+1))/2
    print total
    return tot

f = open('almost-sorted-tc.txt')
n = int(f.readline().strip())
ar = map(int, f.readline().strip().split())
print noOfPos(ar, n)
