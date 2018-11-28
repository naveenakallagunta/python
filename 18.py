a,b=map(int,raw_input(),split())
for i in range(a,b):
	sum=0
	while i>0:
		digit=i%10
	    sum+=digit**3
	    i//=10
	if i==sum:
		print i
