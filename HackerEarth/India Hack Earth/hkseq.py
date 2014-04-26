p,j=input(),0
while j<p:
	t,h,n,i=input(),1,1,2
	while i<t: temp=2014*h+69*n;n,h,i=h,temp,i+1
	print h%(10**9+7);j +=1