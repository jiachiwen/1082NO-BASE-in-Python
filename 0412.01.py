a=int(input())
b=int(input())
c=0
for i in range(a,b):
	if i%2==0:
		continue
	else:
		c=c+i
print(c)
