n=int(input())
A=0
while n>=3:
	A=A+(n//3)
	n=(n//3)+(n%3)
if n==2:
	A=A+1
print(A)






