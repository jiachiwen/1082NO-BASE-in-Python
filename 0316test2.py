a=int(input())
if a>2020:
	print("尚未到來")
elif a<0:
	print("年代久遠")
elif ((a%4==0 and a%100!=0)or a%400==0):
	print("潤年")
else:
	print("非潤年")