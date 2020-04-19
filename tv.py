while True:
	a=int(input())
	b=int(input())
	if a==-1 and b==-1:
		print("")
		break
	else:
		if 0<=a<=100 and 1<=b<=100:
			if abs(a-b)<=50:
				print(abs(a-b))
			else:
				if a>50 and b<50:
					print(abs((100-a))+abs((+b-0)))
				else:
					if a<50 and b>50:
						print(abs((100-b))+abs((a-0)))



