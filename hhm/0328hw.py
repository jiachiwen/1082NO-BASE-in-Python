n = int(input('Place in put a number: '))
if 2 <= n <= 999999999:
	for i in range(2, n):  # 檢查2~n之間的數字是否為質數
		is_prime = True
		for j in range(2, i):  # 檢查 i 是否為質數
			if i % j == 0:
				is_prime = False
				break
		if is_prime:
			if i == 2:
				print(i, end="")
				continue
			print("," + str(i), end="")
else:
	print('不合法')
