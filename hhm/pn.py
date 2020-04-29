""" 
perfect number 完全數

所有因數（不含自己）之和等於自己

例如6 = 1 + 2 + 3
"""


while True:
	n = int(input())
	
	if n == 0:  # 輸入 0 則終止
		break
	
	factors = []  # 因數們
	# 算因數囉
	for i in range(2, n):
		if n % i == 0:
			factors.append(i)
	
	# 算和囉
	amount = 1  # 因數要算入 1
	for j in factors:  # 把所有因數加起來
		amount += int(j)
	
	# 按照要求印出
	if amount == n:
		print("True")
	else:
		print("False")