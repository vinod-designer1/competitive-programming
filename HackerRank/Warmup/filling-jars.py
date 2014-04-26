#https://www.hackerrank.com/challenges/filling-jars
import math
nm = [int(i) for i in raw_input().strip().split(' ')]
m = nm[1]
n = nm[0] * 1.0

tsum = 0

while m > 0:
  ijk = [int(i) for i in raw_input().strip().split(' ')]
  tsum += (ijk[1] - ijk[0] + 1)* ijk[2]
  m -= 1
print int(math.floor(tsum/n))