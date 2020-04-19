element=[]
while True:
	n=int(input())
	if n==0:
		break
	else:
		for i in range(1,n):
			if n%i==0:#確定因數
				element.append(i)
	amount=0#一開始的總和
	for j in element:
		amount=amount+j
	#印出來
	if amount==n:
		print("True")
	else:
		print("False")