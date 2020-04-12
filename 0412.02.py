z=int(input())
for i in range(1,z+1):
	a=int(input())
	b=int(input())
	c=int(input())
	if a+b>c and a+c>b and b+c>a:
		if a==b==c:
			print("Case",i,":E")
		else:
			if a==b!=c or a==c!=b or b==c!=a:
				print("Case",i,":C")
			else:
				print("Case",i,":T")
	else:
		print("Case",i,":I")

			