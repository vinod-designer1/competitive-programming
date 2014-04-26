n = input()
solved = 0
while n > 0:
    s = 0 
    for i in raw_input().strip().split():
        s += int(i)
        
    if s > 1:
        solved += 1
    n -= 1
print solved