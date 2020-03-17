a = float(input("身高"))
b = float(input("體重"))
BMI = b/((a/100)**2)
if BMI<18.5:
	print("過輕")
elif 18.5<=BMI<24:
	print("適中")
else:
	print("過重")
