#https://www.hackerrank.com/challenges/find-point
#http://www.ditutor.com/vec/symmetric_point.html
t = input()

for i in range(t):
  ar = [int(i) for i in raw_input().strip().split()]
  print (-ar[0] + 2 * ar[2]), (-ar[1] + 2 * ar[3])