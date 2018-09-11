n=int(raw_input())
fact=1
if n==0:
	print "1"
elif n>0:
	for m in range(1,n+1):
		fact=fact*m
	print fact
