x= float(input())
y= float(input())
if 10000>=x>0 and 10000>=y>0:
	print("QuadrantI")
else:
	if 10000>=x>0 and -10000<=y<0:
		print("QuadrantIV")
	else:
		if -10000<=x<0 and 10000>=y>0:
			print("QuadrantII")
		else:
			if -10000<=x<0 and -10000<=y<0:
				print("QuadrantIII")
			else:
				if x==0 and y!=0:
					print("y-axis")
				else:
					if y==0 and x!=0:
						print("x-axis")
					else:
						if x==0 and y==0:
							print("origin")