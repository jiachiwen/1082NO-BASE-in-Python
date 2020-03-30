n=int(input())
prime=True
#先找出n的所有因數
#再找出因數中的質數
for i in range(2,n):
	if n%i==0:
		
	for j in range(2,i):
		if i%j==0:
			prime==	False
		