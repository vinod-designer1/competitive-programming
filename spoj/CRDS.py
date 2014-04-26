def cards(n):
	return ((n%(1000007)) * ((n+1)%(1000007)) + ((n-1)%(1000007)) * (n%(1000007)) / 2)

def cards2(n):
	return (n * (n+1) + (n-1) * n / 2)%1000007

t = input()

i = 0
while i < t:
	print cards2(input())
	i += 1
