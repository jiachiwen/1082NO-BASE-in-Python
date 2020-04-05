while True:
	n=int(input())
	prime=True
	for i in range(2,n):#判斷n為質數
		if n%i==0:
			prime=False
			break
	if prime==True:
		break 
	else:
		print(n)
print("end")
		