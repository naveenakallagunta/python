a,b=map(int,raw_input().split())
for num in range(a,b):
    c=0
    for i in range(a,b+1):
        if (num%i==0):
            c=c+1
    if(c==2):
 	print num 
