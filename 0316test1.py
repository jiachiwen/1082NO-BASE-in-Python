a=int(input())
if a%4==0 and a%100!=0:  
	print("潤年")
else:
	if a%400==0:
		print("潤年")
	else:
		print("非潤年")
