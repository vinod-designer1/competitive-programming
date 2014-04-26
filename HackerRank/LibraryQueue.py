# Enter your code here. Read input from STDIN. Print output to STDOUT

t = input()

while t > 0:
    n = input()
    ar = [int(i) for i in raw_input().strip().split()]
    
    q = input()
    
    while q > 0:
        qr = [int(i) for i in raw_input().strip().split()]
        if qr[0] == 0:
            x = qr[1] - 1
            y = qr[2]
            k = qr[3]

            car = [0]*1000

            numu = []

            length = (y-x)+1

            for i in range(x, length):
                if car[i-1] == 0:
                    numu.append(i)
                car[i-1] += 1

            sumn = 0
            for i in numu:
                sumn += car[i-1]

                if sumn >= k:
                    print i
                    break
        else:
            ar[qr[1]-1] = qr[2]
      
        q -= 1
    t -= 1  