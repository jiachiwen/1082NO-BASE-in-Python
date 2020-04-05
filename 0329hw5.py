n=int(input())
if 2<=n<=999999999:
	for i in range(2,n+1):#檢查2~n之間的數字是否為質數
		prime=True
		for j in range(2,i):#檢查i是否為質數
			if i%j==0:
				prime=False
			else:
				if i==2:
					print(i,end="")
#結果還是只印出n