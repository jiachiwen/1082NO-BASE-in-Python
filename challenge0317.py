a=int(input())
b=int(input())
c=int(input())
if a>b and b>c:
	print(a,","b ",",c)
elif b>a and a>c:
	print(b,"," a ",",c)
else:
	print(c,","b ",",a)
	