a=int(raw_input())
fact=1
if a==0:
	print "1"
elif a>0:
	for i in range(1,a+1):
		fact=fact*i
	print fact
