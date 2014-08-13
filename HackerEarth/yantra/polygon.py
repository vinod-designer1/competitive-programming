#http://discuss.codechef.com/questions/4250/swarm-editorial
def find_intersections(n):
	num = 1000000007
	rez = 0
	i = 2
	while i < n-1:
		rez += ((i-1) * (n-1-i))%num
		i += 1
	rez = (rez*n)%num
	rez = (rez*250000002)%num
	return rez

n = input()
print find_intersections(n)

