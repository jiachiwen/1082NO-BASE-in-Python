n=int(input())
A=int(input())
F=int(input())
print(n)
for k in range(0,n):#n代表有幾組，所以不能超過n的範圍
	while True:
		A=int(input())#代表要印出多少次 無法解決：印法(老師出的那題我剛好偷懶沒做)
		F=int(input())#代表重複幾次動作
		for i in range(0,F):
			for j in range(0,A):
				print("*")
				


	