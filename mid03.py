li=[]
while True:
	n=int(input())
	if -10000<=n<=10000 and n!=Exit #無法解決：str()跟int()相容性的問題，導致輸入'Exit'錯誤
		li.append(n)
		li.sort()
		print(li[0],end="")
		print(",",end="")
		print(li[-1])
	else:
		break