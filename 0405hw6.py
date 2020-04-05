A=0
B=0
C=0
while True:
	n=input()
	if n=="end":
		break
	else:
		n=int(n)
		if 0<=n<=100:
			if 85<=n:
				A=A+1
			else:
				if 60<=n<=84:
					B=B+1
				else:
					C=C+1
		else:
			print("超過範圍")
print("A:",A)
print("B:",B)
print("C:",C)

	