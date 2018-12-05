def fibonacci(z):
	if(z<=1):
		return z
	else:
		return(fibonacci(z-1)+fibonacci(z-2))
z=int(raw_input())
print (' ')
for i in range(1,z+1):
	print fibonacci(i),
		
