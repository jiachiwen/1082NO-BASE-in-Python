n=int(input())
li=[]
while True:
	if n==1:
		break
	else:
		if n%2!=0:
			n=n*3+1
			li.append(n)
			li.append('_')#間隔li元素的，同時有,(原本就在list裡)跟_(題目要求放入)
			#添加元素進去li
		else:
			n=n/2
			li.append(n)
			li.append('_')
print(li,end="")#印出 #無法解決:自動取到小數點後一位的問題