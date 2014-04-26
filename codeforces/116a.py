n = input()

p = n

maxp = 0
ins = 0

while n > 0:
    io = [int(i) for i in raw_input().strip().split()]
    o = io[0]
    i = io[1]
    

    ins = i+ins - o
        
    if maxp < ins:
        maxp = ins
    n -= 1
    
print maxp