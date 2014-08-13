n = input()
solved = 0
for i in range(n):
    s = raw_input().strip()
    if s != '0 0 0' and s != '1 0 0' and s != '0 1 0' and s != '0 0 1':
    	solved += 1
print solved