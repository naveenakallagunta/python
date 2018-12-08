z=int(raw_input())
fact=1
if(z==0):
	print 1
else:
	for i in range(1,z+1):
		fact=fact*i
	print fact
