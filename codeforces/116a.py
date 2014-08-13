n = input()
maxp = 0
ins = 0

for i in range(n):
    io = map(int, raw_input().strip().split())
    ins += io[1] - io[0]
        
    if maxp < ins:
        maxp = ins
    
print maxp